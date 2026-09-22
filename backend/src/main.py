from fastapi import FastAPI
from db.connection import DBConnection, Base
from fastapi.middleware.cors import CORSMiddleware

from router.clientes import router as cliente_rota
from router.agendamentos import router as agendamento_rota


from fastapi.middleware.cors import CORSMiddleware # para permitir que o front-end (Vue) acesse a API





db_con = DBConnection()
engine = db_con.get_engine()

Base.metadata.create_all(bind=engine)

app = FastAPI (
    title="API arena society",
    description="backend para gerenciamento de clientes e agendamento de horários.",
    version="1.0.0"
)


app.include_router(cliente_rota)
app.include_router(agendamento_rota)

# configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", 
                   "https://mvjo-code.github.io"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def initial():
    return {
        "aviso": "servidor iniciado com sucesso",
        "status": 200
    }