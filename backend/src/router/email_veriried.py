from fastapi import FastAPI, APIRouter, HTTPException, Header, Request
from db.connection import DBConnection
from db import models
import schemas
import requests
import os
import secrets

from utils import envair_email as contactando

app = FastAPI()
router = APIRouter(prefix="/email", tags=["email"])

# Simulando um banco de dados (na vida real você usaria SQLAlchemy, Prisma, etc.)
banco_de_dados = {}


#WEHOOK PARA RECEBER O RESULTADO FINAL DO EMAILAWESOME
@router.post("/webhooks/resultado")
async def receber_resultado_webhook(
    request: Request, 
    authorization: str = Header(None) # Pega o header "Authorization"
):
    """
    Rota pública que escuta o servidor do EmailAwesome entregar o resultado final.
    """
    
    # 1. Segurança: Verifica se quem "bateu na porta" sabe a senha combinada
    senha_combinada = f"Bearer {os.getenv('MEU_WEBHOOK_SECRET', 'senha_super_secreta_123')}"
    if authorization != senha_combinada:
        raise HTTPException(status_code=401, detail="Erro de autenticação.")

    # 2. Pega o corpo da mensagem enviada pelo EmailAwesome
    dados = await request.json()
    email_avaliado = dados.get("email_address")
    estado_final = dados.get("email_address_status") # Ex: 'deliverable' (válido), 'undeliverable' (inválido), etc.

    # 3. Lógica de Negócio: Atualiza o banco de dados
    if email_avaliado in banco_de_dados:



        if estado_final != "INVALID":
            print(f"O e-mail {email_avaliado} é real!")

            with DBConnection() as  db:
                cliente_existente = db.session.query(models.Cliente).filter(models.Cliente.email == dados.get("email_address")).first()

                if not cliente_existente:
                    raise HTTPException(status_code=500, detail='Cliente não existente, verificação de email não pode ser concluída.')
                
            token_secury = secrets.token_urlsafe(32)
            cliente_existente.token_verificacao = token_secury
            contactando(dados.get("email_address"), token_secury)
            
        else:
            raise HTTPException(status_code=400, detail=f"O e-mail {email_avaliado} é inválido ({estado_final})..")

    # 4. Retorna 200 OK obrigatoriamente
    # Isso avisa o EmailAwesome que você processou a mensagem e eles podem parar de enviar
    return {"status": "ok", "mensagem": "Resultado recebido com sucesso, email de verificação enviado."}



@router.get("/confirmar")

async def confirmar_cadastro(token: str):
 # Rota para integra rusuário após sua confirmação de acesso ao email fornecido
 

    # Procura no banco de dados qual usuário tem esse token exato
    with DBConnection() as db:

        try: 
            cliente_existente = db.session.query(models.Cliente).filter(models.Cliente.token_verificacao == token).first()

            if not cliente_existente:
                raise HTTPException(status_code=500, detail='Cliente não existente, verificação de email não pode ser concluída.')

            # atualiza status do cliente
            cliente_existente.amail_verificado = "VALID"
            cliente_existente.token_verificacao = None

            return {"status_code": 200, "mensagem": "Conta ativada com sucesso! Você já pode fazer login."}

        
        except Exception as error:  # Se o token não existir (ou já tiver sido usado)
            db.session.rollback()

            raise HTTPException(status_code=400, detail=f"Link inválido ou já expirado. Details: {str(error)}")

