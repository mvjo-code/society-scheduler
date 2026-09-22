
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base

# mapeamento declarativo a partir da Base declarativa

#tabelas

class Cliente(Base):
    ''' para o cliente'''
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    rua = Column(String, nullable=False)
    n_casa = Column(String, nullable=False)
    senha_hash = Column(String, nullable=False)

    agendamentos = relationship("Agendamento", back_populates="cliente")

    def __repr__(self):
        return f"Cliente(id = {self.id}, nome = '{self.nome}', telefone = '{self.telefone}')"

class Agendamento(Base):
    '''para o agendamento'''

    __tablename__="agendamentos"

    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    data_hora_inicio = Column(DateTime, nullable=False)
    data_hora_final = Column(DateTime, nullable=False)
    status = Column(String, default="pendente")
    preco = Column(Float, nullable=False)

    cliente = relationship("Cliente", back_populates="agendamentos")
    
    def __repr__(self):
        return f"Agendamento(id = {self.id}, cliente_id = {self.id_cliente}, status = '{self.status}')"