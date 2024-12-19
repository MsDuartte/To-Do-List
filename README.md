# To-Do List

Além do CRUD em Python e Django e toda a lógica de programação envolvida, a minha ideia com esse projeto foi criar um gerenciador de tarefas baseado em uma das metodologias ágeis que temos hoje: o Kanban.

## Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Uso](#uso)
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
   python -m venv env

3. Instale as dependências:
  pip install -r requirements.txt

4. Faça as migrações:
  python manage.py makemigrations
  python manage.py migrate

5. Execute o codigo:
  python manage.py runserver

## Contato
Matheus Santos Duarte
E-mail: msduarte.matheus@gmail.com
Linkedin: https://www.linkedin.com/in/matheus-duarte-53601a144/
   
