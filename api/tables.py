from sqlalchemy import Column, Integer, String, DateTime, create_engine, Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Totem(Base):
    __tablename__ = 'totem'

    id = Column(Integer, primary_key=True)
    status = Column(String(50), nullable=False)
    data_hora = Column(DateTime, nullable=False, default=datetime.now())  # Define valor padrão como a data e hora atual

class UsuariosSistema(Base):
    __tablename__ = 'usuarios_sistema'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    status = Column(Boolean, nullable=False)