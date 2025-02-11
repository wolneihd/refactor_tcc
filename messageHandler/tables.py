from sqlalchemy import Column, Integer, String, Text, Boolean, create_engine, ForeignKey, BigInteger
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Tabela Usuario (tabela "pai")
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)  # Chave primária
    nome = Column(String(255), nullable=False)  # Especificando o comprimento máximo
    sobrenome = Column(String(255), nullable=False)  # Especificando o comprimento máximo
    userID_Telegram = Column(BigInteger, nullable=False)

    # Relacionamento com a tabela Mensagem
    mensagens = relationship("Mensagem", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', sobrenome='{self.sobrenome}, userID_Telegram'{self.userID_Telegram}')>"

# Tabela Mensagem (tabela "filha")
class Mensagem(Base):
    __tablename__ = 'mensagens'

    id = Column(Integer, primary_key=True)  # Chave primária
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))  # Chave estrangeira
    texto_msg = Column(String(255), nullable=False)
    timestamp = Column(Integer, nullable=False)
    tipo_mensagem = Column(String(255), nullable=False)
    respondido = Column(Boolean, nullable=False)

    # Colunas campos IA
    llm_id = Column(Integer, ForeignKey('llm.id'))  # Chave estrangeira
    analise_ia = Column(String(255), nullable=True)
    categoria = Column(String(255), nullable=True)
    feedback = Column(String(255), nullable=True)
    resposta = Column(String(255), nullable=True)

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="mensagens")
    llm = relationship("LLM", back_populates="mensagens")  # Correção no back_populates

# Tabela LLM (tabela "filha")
class LLM(Base):
    __tablename__ = 'llm'

    id = Column(Integer, primary_key=True)  # Chave primária
    llm = Column(String(50), nullable=False)

    # Relacionamento com a tabela Mensagem
    mensagens = relationship("Mensagem", back_populates="llm")  # Correção no nome do relacionamento

class Configs(Base):
    __tablename__ = 'configs'

    id = Column(Integer, primary_key=True)  # Chave primária
    campo = Column(String(50), nullable=False)
    valor = Column(String(50), nullable=False)