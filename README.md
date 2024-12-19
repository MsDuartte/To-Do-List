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

![Tela de Registro](https://github.com/user-attachments/assets/1daaa373-0f6b-478a-8fb1-f4399b31cc28)

![Lista de Tarefas](https://github.com/user-attachments/assets/f04d4657-2e06-4594-a1b5-b2a4f6e79bba)

![Criar tarefa](https://github.com/user-attachments/assets/4e47f986-6afe-46f0-8a2e-06569e775926)

![Detalhes da Tarefa](https://github.com/user-attachments/assets/5e850dda-7758-4791-a1b0-69f8a48dbcc1)

![Editar Tarefa](https://github.com/user-attachments/assets/e467c682-0658-4f59-9da9-d1a3c2c7a3cb)

![Alteração do status da tarefa](https://github.com/user-attachments/assets/f28a3de7-a019-4fe2-b821-7d33042f98b2)

![Deletar Tarefa](https://github.com/user-attachments/assets/9cc74240-49c7-4404-b461-f4f1a9789736)






   
