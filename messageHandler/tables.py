from sqlalchemy import Column, Integer, String, Text, Boolean, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Tabela Usuario (tabela "pai")
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)  # Chave primária
    nome = Column(String(255), nullable=False)  # Especificando o comprimento máximo
    sobrenome = Column(String(255), nullable=False)  # Especificando o comprimento máximo
    userID_Telegram = Column(Integer, nullable=False)

    # Relacionamento com a tabela Mensagem
    mensagens = relationship("Mensagem", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', sobrenome='{self.sobrenome}, userID_Telegram'{self.userID_Telegram}')>"

# Tabela Mensagem (tabela "filha")
class Mensagem(Base):
    __tablename__ = 'mensagens'

    id = Column(Integer, primary_key=True)  # Chave primária
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))  # Chave estrangeira
    texto_msg = Column(String(255), nullable=False)  # Especificando o comprimento máximo
    timestamp = Column(Integer, nullable=False)
    tipo_mensagem = Column(String(255), nullable=False)  # Especificando o comprimento máximo

    # Colunas campos IA
    analise_ia = Column(String(255), nullable=True)  # Especificando o comprimento máximo
    categoria = Column(String(255), nullable=True)  # Especificando o comprimento máximo
    feedback = Column(String(255), nullable=True)  # Especificando o comprimento máximo

    # Relacionamento com a tabela Usuario
    usuario = relationship("Usuario", back_populates="mensagens")