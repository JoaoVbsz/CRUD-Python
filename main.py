from sqlalchemy.orm import Session
from db import SessionLocal
from models import User
from crud import create_user, list_users, get_user, delete_user
from datetime import datetime

db = SessionLocal()

print("=== Cadastro de Novo Usuário ===")
nome = input("Nome completo: ")
data_nasc_str = input("Data de nascimento (AAAA-MM-DD): ")
genero = input("Gênero: ")
cpf = input("CPF: ")
email = input("Email: ")
cep = input("CEP: ")

data_nascimento = datetime.strptime(data_nasc_str, "%Y-%m-%d").date()

novo = User(
    nome_completo=nome,
    data_nascimento=data_nascimento,
    genero=genero,
    cpf=cpf,
    email=email,
    cep=cep
)

# Inserir no banco
create_user(db, novo)
print("Usuário cadastrado com sucesso!")


# Listar usuários
users = list_users(db)
for u in users:
    print(f"ID: {u.id}, Nome: {u.nome_completo}")


# get_user(db, id = "c9f082ab-b7df-4ad3-b542-2c1b862d57d6", novo_nome= "Ana Maria Costa")

# delete_user(db, id="c9f082ab-b7df-4ad3-b542-2c1b862d57d6")

db.close()
