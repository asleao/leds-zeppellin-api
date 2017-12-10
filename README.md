# leds-zeppelin [![Build Status](https://travis-ci.org/asleao/leds-zeppelin.svg?branch=master)](https://travis-ci.org/asleao/leds-zeppelin)

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
