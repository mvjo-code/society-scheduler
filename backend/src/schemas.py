from pydantic import BaseModel
from datetime import datetime

# SCHEMAS PARA CLIENTE


class ClienteBase(BaseModel):
    nome: str
    telefone: str
    cidade: str
    bairro: str
    rua: str
    n_casa: str
    email: str
    

# Molde de Entrada (O que o Vue.js envia)
class ClienteCreate(ClienteBase):
     senha_hash: str

# 3. Molde de Saída (O que a API devolve para o Vue.js)
class ClienteResponse(ClienteBase):
    id: int

    # Essa configuração avisa ao Pydantic para saber ler os objetos do SQLAlchemy
    class Config:
        from_attributes = True

class ClienteLogin(BaseModel):
    email: str
    senha: str


# schema para agendamento

class AgendamentoBase(BaseModel):
    data_hora_inicio: datetime
    data_hora_final : datetime
    status: str

class AgendamentoCreate(AgendamentoBase):
    pass

class AgendamentoResponse(AgendamentoBase):
    id: int
    preco: float

    class Config:
        from_attributes = True