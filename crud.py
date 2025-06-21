from models import User
from sqlalchemy.orm import Session
from uuid import UUID

def create_user(db: Session, dados: dict):
    user = User(
        nome_completo=dados.nome_completo,
        data_nascimento = dados.data_nascimento,
        genero=dados.genero,
        cpf=dados.cpf,
        email=dados.email,
        cep=dados.cep
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def list_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, id: UUID, novo_nome: str):
    user = db.query(User).filter(User.id == id).first()
    if user:
        user.nome_completo = novo_nome
        db.commit()
    return user
    
def delete_user(db: Session, id: int):
    
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()

        return user
