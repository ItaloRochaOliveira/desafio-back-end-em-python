# desafio-back-end-em-python

## 📖 Introdução

O desafio back end em python é uma API feita com o intuito de cadastrar, editar e deletar cadastro de profissionais da saúde, onde é possível informar nome e nome social. Também é possível cadastrar, editar e eliminar consultas vinculadas a um desses profissionais. Por fim, é possível pesquisar todas as consultas vinculada a um profissional.

Fiz o uso de arquitetura em camadas com o conhecimento adquirido até então e por ser uma arquitetura considerada fácil, rápida de ser projetada e entendida.

Os conteúdos principais a serem estudados são:

- Conceito de python.
- Criação de uma API.
- Conter todos os principais métodos: get, post, put e delete.
- Arquitetura em camadas.
- Programação Orientada a Objeto.

## 🔗Link de Acesso

- Documentação: [clique aqui!](https://documenter.getpostman.com/view/25826643/2s93si1Vup).
- STATUS: EM PROCESSO...

## 📄Concepção do Projeto

### Instalando

```bash
# Instalando dependências
pip install

# executando o projeto
venv/Scripts/activate
python index.py run
```

### Funcionalidades

```bash
. Requisições:
- getAppointmentByIdProfessional: Pesquisar todas as consultas relacionada a um id 
de um profissional.
- createAppointment: Criar consultas informando a data da consulta e informando um 
id de um profissional para vincular eles.
- updateAppointment: Atualizar consultas já cadastradas, atualizando a data, e 
informando o id da consulta.
- deleteAppointment: Deletar consultas existentes informando seu id.

- createProfessional: Cadastrar um profissional informando seu nome e, se houve, 
o nome social.
- updateProfessional: Atualizar cadastro do profissional, podendo atualizar seu 
nome e nome social.
- deleteProfessional: Deletar profissional cadastrado.
```

### Bibliotecas Utilizadas

```bash
alembic
banal
blinker
click
colorama
dataset
Flask
greenlet
itsdangerous
Jinja2
Mako
MarkupSafe
SQLAlchemy
typing_extensions
uuid
Werkzeug

```

## 💡Programas utilizados:

- VSCode
- PostMan

## 💻Tecnologias

![python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)


## 📫 Contato

<p>Email: italo.rocha.de.oliveira@gmail.com</p>
<a href = "mailto:italo.rocha.de.oliveira@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" alvo ="_blank"></a>
<a href="https://www.linkedin.com/in/italorochaoliveira/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
