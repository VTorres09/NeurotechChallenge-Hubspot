# Neurotech CRUD - HubSpot

![Vue Logo](/src/assets/logo-vue.png "Vue Logo")
![Django Logo](/src/assets/logo-django.png "Django Logo")

Esse projeto foi criado para o Desafio de Engenharia de Software da Neurotech.

Vue e Django estão claramente separados neste projeto. Vue, Yarn e Webpack tratam de toda a lógica de front-end e avaliações de empacotamento. Django e Django REST framework para gerenciar modelos de dados, API Web e servir arquivos estáticos.

Enquanto é possível adicionar endpoints para servir respostas html renderizadas por django, a intenção é usar Django principalmente para o back-end (fazendo o link com a API do Hubspot), e ter a renderização e o roteamento de visualização e serem gerenciados pelo Vue + Vue Router como um aplicativo de página única (SPA).

Django servirá o ponto de entrada do aplicativo (`index.html` + ativos agrupados) em  `/`,
dados em `/api/`, e arquivos estáticos em `/static/`. O painel de administração do Django também está disponível em `/admin/`.

### Funcionalidades do Sistema

A lista de contatos cadastrados no Hubspot será exibida na lista com Nome, Data de Nascimento, Email,Telefone e Peso (Kg). Para cadastrar ou atualizar basta clicar no botão de adicionar contato e preencher os campos necessários, caso deseje atualizar, deve preencher o formulário colocando o mesmo email.

Para conectar com sua conta no hubspot basta substituir o valor da variável API_KEY que se encontra no arquivo `backend/api/views.py`.

### Estrutura do Projeto

| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/backend`           | Django Project & Backend Config            |
| `/backend/api`       | Django App (`/api`)                        |
| `/src`               | Vue App .                                  |
| `/src/main.js`       | JS Application Entry Point                 |
| `/public/index.html` | [Html Application Entry Point](https://cli.vuejs.org/guide/html-and-static-assets.html) (`/`)         |
| `/public/static`     | Static Assets                              |

## Pre-requisitos

Antes de rodar o projeto você deve ter os seguintes pacotes instalados:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install)
- [X] Vue CLI 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3 - [instructions](https://wiki.python.org/moin/BeginnersGuide)
- [X] Pipenv - [instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)

## Configuracao do Projeto

```
$ git clone https://github.com/gtalarico/django-vue-template
$ cd django-vue-template
```

```
$ yarn install
$ pipenv install --dev && pipenv shell
$ python manage.py migrate
```

## Rodando o servidor

```
$ python manage.py runserver
```

De outra tab no mesmo diretório rode:

```
$ yarn serve
```

A aplicação Vue ficará disponivel em [`localhost:8080`](http://localhost:8080/) e a API do Django
com os arquivos estaticos em [`localhost:8000`](http://localhost:8000/).
