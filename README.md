# To-Do List

Além do CRUD em Python e Django e toda a lógica de programação envolvida, a minha ideia com esse projeto foi criar um gerenciador de tarefas baseado em uma das metodologias ágeis que temos hoje: o Kanban.

## Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Contato](#contato)

## Descrição

Esta aplicação foi desenvolvida para ajudar os usuários a gerenciar suas tarefas diárias de forma eficiente. Com uma interface simples e intuitiva, os usuários podem adicionar novas tarefas, marcar tarefas como concluídas e remover tarefas que não são mais necessárias.

## Funcionalidades

- Adicionar novas tarefas
- Alterar status da tarefa para: Nova, Em Andamento e Concluída
- Deletar tarefas
- Todas as tarefas são salvas no PostgreSQL ou, se preferir, no próprio db.sqlite3 do Django.

## Instalação

Para executar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/MsDuartte/To-Do-List.git

2. Crie o Ambiente virtual:
   ```bash
   python -m venv env

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt

6. Faça as migrações:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

8. Execute o codigo:
   ```bash
   python manage.py runserver

## Contato
Matheus Santos Duarte

E-mail: msduarte.matheus@gmail.com

Linkedin: https://www.linkedin.com/in/matheus-duarte-53601a144/

## Preview


![Tela de Login](https://github.com/user-attachments/assets/60c8b258-d951-4bc6-a307-f1e09b5fe8bc)

   
