- Nome: Valmir Carlos Cerutti Neto
- CPF: 090.454.516-46
- Email: vcceruttineto@gmail.com
- Número: 31 9 8668-0288

## 1. Como utilizar o app:

    Para executar a aplicação com as configurações padrão:

    python src/main.py
    A aplicação irá:

        Autenticar-se automaticamente na API
        Buscar as baterias agendadas para o email padrão (john.doe@gmail.com)
        Exibir as baterias futuras
        Aguardar interação do usuário

    Você pode modificar o email padrão editando a linha no arquivo src/main.py:

        email = "john.doe@gmail.com"  # Altere para o email desejado


    Após a exibição inicial, o sistema apresentará as seguintes opções:

        Digite 'ver passadas' para visualizar as baterias já realizadas
        Digite 'sair' para encerrar a aplicação

## 2. Funções Disponíveis

__init__(self)
    Descrição: Inicializa a classe com as configurações básicas
    Parâmetros: Nenhum
    Retorno: Nenhum

authenticate(self)
    Descrição: Realiza a autenticação na API e obtém o token JWT
    Parâmetros: Nenhum
    Retorno:
    True se a autenticação for bem-sucedida
    False em caso de falha

query_baterias(self, email)
    Descrição: Consulta as baterias associadas a um email específico
    Parâmetros:
    email (str): Email do cliente a ser consultado
    Retorno:
    Lista de dicionários com os dados das baterias em caso de sucesso
    None em caso de falha

process_baterias(data)
    Descrição: Método estático que processa e classifica as baterias
    Parâmetros:
    data (list): Lista de baterias retornadas pela API
    Retorno:
    Tupla com (baterias_futuras, baterias_passadas)

format_message(baterias_futuras, baterias_passadas, show_past=False)
    Descrição: Formata a mensagem de saída para o usuário
    Parâmetros:
    baterias_futuras (list): Baterias agendadas para o futuro
    baterias_passadas (list): Baterias já realizadas
    show_past (bool): Se True, inclui as baterias passadas na mensagem
    Retorno:
    String formatada com a mensagem para o usuário

## 3. Processo de Build e Deploy

    Build (Preparação do Ambiente)

        1. Clone o repositório
        git clone https://github.com/seu-usuario/repositorio.git
        cd repositorio

        2. Instale a única dependência necessária
        pip install requests

    Deploy (Execução)

        Execute o programa com:
        python src/main.py