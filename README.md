
# Mini Projeto Flask - Registro e Acompanhamento de Logs

## Descrição

Este é um mini projeto em Flask para criar uma aplicação web que permite autenticação de um único usuário para acompanhamento e registro de logs via requisições HTTP. A aplicação foi desenvolvida para facilitar o gerenciamento de logs de diferentes sistemas, permitindo ao usuário monitorar e manter o histórico de eventos em tempo real. Esta versão do projeto permite apenas um usuário, mas é escalável e pode ser adaptada para suportar múltiplos usuários, dashboards e outras funcionalidades, dependendo da criatividade e necessidades de cada usuário.

## Recursos

-   Autenticação de um único usuário
-   Acompanhamento de logs em tempo real
-   Registro de logs via requisições HTTP
-   Interface web simples e intuitiva


## Pré-requisitos

Antes de começar, certifique-se de ter instalado em seu ambiente:

-   Python 3.6+
-   Flask 1.1.2+
-   Flask-SQLAlchemy 2.5.1+
-   Flask-Login 0.5.0+
-   Flask-WTF 0.15.1+

## Instalação

1.  Clone o repositório:

`git clone https://github.com/macolym/app-logs-flask.git
cd app-logs-flask` 

2.  Crie um ambiente virtual e instale as dependências:

`python -m venv venv
source venv/bin/activate
pip install -r requirements.txt` 

3.  Configure as variáveis de ambiente necessárias:

`export USERNAME=username
export PASSWORD=password
export JWT_SECRET=jwt_secret
export CLIENT_SECRET=client_secret
export SECRET_KEY=secret_key` 

Observação: É possível realizar alterações na aplicação Flask com um pouco de conhecimento técnico, no entanto, as regras mencionadas acima foram implementadas devido à necessidade de manter a segurança rígida em nossos servidores. Por favor, tenha cuidado ao fazer quaisquer alterações e certifique-se de que elas não comprometam a segurança da aplicação.

4.  O banco de dados SQLite é criado automaticamente, execute o servidor com o comando abaixo:

`flask run` 

A aplicação estará disponível em `http://localhost:5000`.

## Uso

1.  Faça login na aplicação utilizando as credenciais informadas na variável de ambiente.
2.  Para registrar novos logs, envie uma requisição HTTP POST para a rota `/add_log` com as informações do log no corpo da requisição.
3.  Acesse a página de acompanhamento de logs para visualizar os logs registrados.

## Contribuição

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](https://chat.openai.com/c/LICENSE) para mais detalhes.