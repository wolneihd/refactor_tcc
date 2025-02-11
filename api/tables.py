from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Totem(Base):
    __tablename__ = 'totem'

    id = Column(Integer, primary_key=True)
    status = Column(String(50), nullable=False)
    data_hora = Column(DateTime, nullable=False, default=datetime.now(datetime.timezone.utc))  # Define valor padrão como a data e hora atual
