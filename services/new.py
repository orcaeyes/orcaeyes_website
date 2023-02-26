from db import get_session
from models.new import New
from sqlalchemy import desc


def create_new():
    pass

def delete_new():
    pass

def get_news() -> list:
    with get_session() as session:
        return session.query(New).order_by(desc(New.created_at)).all()

def get_new(id):
    with get_session() as session:
        return session.query(New).filter_by(id=id).first()