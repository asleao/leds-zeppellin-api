# leds-zeppelin [![Build Status](https://travis-ci.org/asleao/leds-zeppellin-api.svg?branch=feature%2FLZ-MODELS)](https://travis-ci.org/asleao/leds-zeppellin-api)

Repositório para o desenvolvimento do sistema LedsZeppelin.


### Docker

#### Pré-Requisitos:
* **Docker**
* **Docker Compose**

Entre na pasta do projeto e digite os seguintes comandos:

    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser

Para rodar o projeto digite o comando:

    docker-compose up
   
   
## Configuração das variáveis de ambiente

Adicione as seguintes variáveis de ambiente:

export PG_DATABASE= '<nome_banco>'
export PG_USER='<nome_usuario>'
export PG_PASS='<password>'
export PG_PORT='<porta_banco>'
export EMAIL_HOST='smtp.gmail.com'
export EMAIL_HOST_PASSWORD='<password_email>'
export EMAIL_HOST_USER='<email>'
export EMAIL_PORT='587'
export EMAIL_USE_TLS='True'
export CLOUDAMQP_URL="<amq_url>"

No linux elas deve estar no arquivo ".bashrc" ou ".zshrc" dependendo do shell que utilizar.

## Pycharm

No pycharm instale o plugin envFiles, em seguida crie um arquivo com o nome **.environment.env** e adicione as variáveis de ambiente da seguinte maneira:

PG_DATABASE= '<nome_banco>'
PG_USER='<nome_usuario>'
PG_PASS='<password>'
PG_PORT='<porta_banco>'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_PASSWORD='<password_email>'
EMAIL_HOST_USER='<email>'
EMAIL_PORT='587'
EMAIL_USE_TLS='True'
CLOUDAMQP_URL="<amq_url>"

Feito isso, basta adicionar o arquivo na aba **EnvFile** da sua configuração de run/debug.

### Login

O sistema utiliza authenticação com JWT, para realizar os testes, baixe o addon "Modheader", realize o login no endpoint "/login" e copie o token retornado. Em seguida abra o Modheader e adicione um request header com o nome "Authorization" e no valor coloque "Bearer <token_copiado>". Dessa forma os endpoints do sistema que requerem autheticação poderam ser acessados.