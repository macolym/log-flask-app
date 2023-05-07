
# Mini Projeto Flask - Registro e Acompanhamento de Logs

## Descri��o

Este � um mini projeto em Flask para criar uma aplica��o web que permite autentica��o de um �nico usu�rio para acompanhamento e registro de logs via requisi��es HTTP. A aplica��o foi desenvolvida para facilitar o gerenciamento de logs de diferentes sistemas, permitindo ao usu�rio monitorar e manter o hist�rico de eventos em tempo real. Esta vers�o do projeto permite apenas um usu�rio, mas � escal�vel e pode ser adaptada para suportar m�ltiplos usu�rios, dashboards e outras funcionalidades, dependendo da criatividade e necessidades de cada usu�rio.

## Recursos

-   Autentica��o de um �nico usu�rio
-   Acompanhamento de logs em tempo real
-   Registro de logs via requisi��es HTTP
-   Interface web simples e intuitiva


## Pr�-requisitos

Antes de come�ar, certifique-se de ter instalado em seu ambiente:

-   Python 3.6+
-   Flask 1.1.2+
-   Flask-SQLAlchemy 2.5.1+
-   Flask-Login 0.5.0+
-   Flask-WTF 0.15.1+

## Instala��o

1.  Clone o reposit�rio:

`git clone https://github.com/macolym/app-logs-flask.git
cd app-logs-flask` 

2.  Crie um ambiente virtual e instale as depend�ncias:

`python -m venv venv
source venv/bin/activate
pip install -r requirements.txt` 

3.  Configure as vari�veis de ambiente necess�rias:

`export USERNAME=username
export PASSWORD=password
export JWT_SECRET=jwt_secret
export CLIENT_SECRET=client_secret
export SECRET_KEY=secret_key` 

Observa��o: � poss�vel realizar altera��es na aplica��o Flask com um pouco de conhecimento t�cnico, no entanto, as regras mencionadas acima foram implementadas devido � necessidade de manter a seguran�a r�gida em nossos servidores. Por favor, tenha cuidado ao fazer quaisquer altera��es e certifique-se de que elas n�o comprometam a seguran�a da aplica��o.

4.  O banco de dados SQLite � criado automaticamente, execute o servidor com o comando abaixo:

`flask run` 

A aplica��o estar� dispon�vel em `http://localhost:5000`.

## Uso

1.  Fa�a login na aplica��o utilizando as credenciais informadas na vari�vel de ambiente.
2.  Para registrar novos logs, envie uma requisi��o HTTP POST para a rota `/add_log` com as informa��es do log no corpo da requisi��o.
3.  Acesse a p�gina de acompanhamento de logs para visualizar os logs registrados.

## Contribui��o

Contribui��es s�o sempre bem-vindas! Sinta-se � vontade para abrir issues ou enviar pull requests.

## Licen�a

Este projeto est� licenciado sob a licen�a MIT. Veja o arquivo [LICENSE](https://chat.openai.com/c/LICENSE) para mais detalhes.