import requests
from datetime import datetime

class KartodromoAPI:
    def __init__(self):
        self.base_url = "https://appsaccess.automy.com.br"
        self.token = None
        self.headers = {
            "Content-Type": "application/json"
        }
    
    def authenticate(self):
        """Autentica na API e obtém token JWT"""
        auth_url = f"{self.base_url}/login"
        auth_data = {
            "username": "fldoaogopdege",
            "password": "ygalepsm"
        }
        
        try:
            response = requests.post(auth_url, json=auth_data, headers=self.headers)
            response.raise_for_status()
            self.token = response.json().get("token")
            self.headers["Authorization"] = f"Bearer {self.token}"
            return True
        except requests.exceptions.RequestException as e:
            print(f"Erro na autenticação: {e}")
            return False
    
    def query_baterias(self, email):
        """Consulta as baterias para um email específico"""
        if not self.token:
            if not self.authenticate():
                return None
        
        query_url = f"{self.base_url}/api/api/desafio/custom/do/query"
        query = f"SELECT * FROM desafio.cadastro_baterias_desafio WHERE email = '{email}'"
        
        query_data = {
            "query": query,
            "db": "desafio"
        }
        
        try:
            response = requests.post(query_url, json=query_data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na consulta: {e}")
            return None
    
    @staticmethod
    def process_baterias(data):
        """Processa os dados das baterias, separando em futuras e passadas"""
        if not data:
            return None, None
        
        hoje = datetime.now()
        baterias_futuras = []
        baterias_passadas = []
        
        for bateria in data:
            try:
                data_bateria = datetime.strptime(bateria["data_agendamento"], "%d/%m/%Y")
                
                if data_bateria >= hoje:
                    baterias_futuras.append(bateria)
                else:
                    baterias_passadas.append(bateria)
            except (ValueError, KeyError):
                continue
        
        return baterias_futuras, baterias_passadas
    
    @staticmethod
    def format_message(baterias_futuras, baterias_passadas, show_past=False):
        """Formata a mensagem para o cliente"""
        message = "Informações sobre suas baterias:\n\n"
        
        if baterias_futuras:
            message += "🚀 Próximas baterias agendadas:\n"
            for i, bateria in enumerate(baterias_futuras, 1):
                message += (
                    f"{i}. Data: {bateria['data_agendamento']} "
                    f"às {bateria['horario_agendamento']}\n"
                    f"   Nome: {bateria['nome']}\n"
                    f"   Pessoas: {bateria['qtde_pessoas']}\n\n"
                )
        else:
            message += "ℹ️ Não há baterias futuras agendadas.\n\n"
        
        if show_past and baterias_passadas:
            message += "⏰ Baterias passadas:\n"
            for i, bateria in enumerate(baterias_passadas, 1):
                message += (
                    f"{i}. Data: {bateria['data_agendamento']} "
                    f"às {bateria['horario_agendamento']}\n"
                    f"   Nome: {bateria['nome']}\n"
                    f"   Pessoas: {bateria['qtde_pessoas']}\n\n"
                )
        elif baterias_passadas:
            message += (
                "\nDigite 'ver passadas' para visualizar suas baterias anteriores.\n"
            )
        
        return message


def main():
    api = KartodromoAPI()
    email = "john.doe@gmail.com"  # Email padrão do desafio
    
    # Obter dados da API
    data = api.query_baterias(email)
    if not data:
        print("Não foi possível obter os dados das baterias.")
        return
    
    # Processar dados
    futuras, passadas = api.process_baterias(data)
    
    # Mostrar mensagem inicial
    print(api.format_message(futuras, passadas))
    
    # Opção para ver passadas
    while True:
        user_input = input("\nO que deseja fazer? ('ver passadas' ou 'sair'): ").strip().lower()
        if user_input == 'ver passadas':
            print(api.format_message(futuras, passadas, show_past=True))
        elif user_input == 'sair':
            break
        else:
            print("Comando não reconhecido. Tente novamente.")


if __name__ == "__main__":
    main()