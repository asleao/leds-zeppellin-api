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

### Login

O sistema utiliza authenticação com JWT, para realizar os testes, baixe o addon "Modheader", realize o login no endpoint "/login" e copie o token retornado. Em seguida abra o Modheader e adicione um request header com o nome "Authorization" e no valor coloque "Bearer <token_copiado>". Dessa forma os endpoints do sistema que requerem autheticação poderam ser acessados.