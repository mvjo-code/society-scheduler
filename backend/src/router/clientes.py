from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
import requests

# importando arquivos criados
from db import models
from db.connection import DBConnection
import schemas
from utils import security

router = APIRouter(prefix="/cliente", tags=["clientes"])


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    with DBConnection() as db:

        cliente = db.session.query(models.Cliente).filter(models.Cliente.email == form_data.username).first()

        if not cliente or not security.verificar_senha(form_data.password, cliente.senha_hash):
            raise HTTPException(
                status_code=401,
                detail=f"Email ou Senha incorretos."
            )

        token = security.criar_token_de_acesso({"sub": form_data.username})

        return {
            "access_token": token,
            "token_type": "bearer"
        }


@router.get("/me", response_model=schemas.ClienteResponse)
def perfil_cliente(email_cliente: str = Depends(security.obter_usuario_atual)):
    
    with DBConnection() as db:
        # Usa o e-mail devolvido pelo segurança para achar o cliente
        cliente = db.session.query(models.Cliente).filter(models.Cliente.email == email_cliente).first()

        if not cliente:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        return cliente




@router.get("/ativos")
def listar_ativos():
    return {"messasge": "rota para listar clientes ativos"}



@router.get("/", response_model=list[schemas.ClienteResponse])
def listar_clientes():
    ''' funcao para listar clientes'''
    try:
        with DBConnection() as db:

            todos_os_clientes = db.session.query(models.Cliente).all()
            return todos_os_clientes

    except Exception as error:
        raise HTTPException(
            status_code=404,
            detail= f"erro ao buscar clientes. Detahes: {str(error)}"
        )
        
@router.get("/{id}", response_model=schemas.ClienteResponse)
def detalhes_cliente(id: int):

    with DBConnection() as db:

        cliente = db.session.query(models.Cliente).filter(models.Cliente.id == id).first()

        if not cliente:
            raise HTTPException(status_code=404, detail="Este usuário não existe.")

        return cliente
        
@router.put("/{id}", response_model=schemas.ClienteResponse)
def atualizar_dados_cliente(id: int, novos_dados: schemas.ClienteCreate):

    with DBConnection() as db:
        cliente = db.session.query(models.Cliente).filter(models.Cliente.id == id).first()

        if not cliente:
            raise HTTPException(status_code=404, detail="Este usuário não existe.")

        cliente.nome = novos_dados.nome
        cliente.email = novos_dados.email
        cliente.senha_hash = security.gerar_hash_senha(novos_dados.senha_hash)
        cliente.telefone = novos_dados.telefone
        cliente.cidade = novos_dados.cidade
        cliente.bairro = novos_dados.bairro
        cliente.rua = novos_dados.rua
        cliente.n_casa = novos_dados.n_casa

        try:

            db.session.commit()
            db.session.refresh(cliente)

            return cliente

        except Exception as error:
            db.session.rollback()
            raise HTTPException(status_code=500, detail=f"Não foi possível conectar-se ao banco. Detalhes: {str(error)}")




@router.post("/", response_model=schemas.ClienteResponse)
def adicionar_cliente(data_cliente : schemas.ClienteCreate):
    '''funcao para cadastrar clientes
    
        autenticação do email cadastrado é feita nessa função, chamando a API do EmailAwesome
    '''
        
    with DBConnection() as db:


        cliente_existente = db.session.query(models.Cliente).filter(
            (models.Cliente.telefone == data_cliente.telefone) | 
            (models.Cliente.email == data_cliente.email)
        ).first()

        if cliente_existente:
            raise HTTPException(status_code = 400, detail = "cliente já existente")

        # autenticação
        snh = security.gerar_hash_senha(data_cliente.senha_hash)


        novo_cliente = models.Cliente (
            nome=data_cliente.nome,
            telefone=data_cliente.telefone,
            cidade = data_cliente.cidade,
            bairro=data_cliente.bairro,
            rua=data_cliente.rua,
            n_casa=data_cliente.n_casa,
            senha_hash=snh,
            email=data_cliente.email,
            email_verificado=data_cliente.email_verificado
        )

        try:

            db.session.add(novo_cliente)
            db.session.commit()
            db.session.refresh(novo_cliente)
            return novo_cliente
        
        except Exception as error:

            db.session.rollback()
            
            raise HTTPException(
                status_code=500,
                detail=f"não foi possível cadastrar o cliente, details: {str(error)}"
            )

        #  autenticação do email cadastrado
        # Faz o pedido para a API do EmailAwesome
    try:
        requests.post(
            "https://api.emailawesome.com/api/validations/email_validation",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-api-key": API_KEY,
            },
            json={
                "email": data_cliente.email,
                "results_callback": {
                    "url": URL_DO_SEU_WEBHOOK,
                    "method": "POST",
                    "headers": {
                        "Authorization": f"Bearer {WEBHOOK_SECRET}"
                    }
                }
            },
            timeout=10
        )

        # Não precisamos ler o response.json() aqui porque sabemos que vai dar "PENDING"
    except requests.exceptions.RequestException as e:
        # Se a API deles cair, você não trava o seu sistema
        raise HTTPException(status_code=500, detail=f"Erro na API de email: {e}")

    # 3. Libera a tela do usuário na mesma hora! (Resposta Imediata Ilusória)
    return {
        "mensagem": "Cadastro recebido! Estamos preparando sua conta. Verifique sua caixa de entrada em alguns instantes.",
        "email": data_cliente.email
    }

@router.delete("/{id}")
def deletar_cliente(id: int):

    with DBConnection() as db:
        cliente = db.session.query(models.Cliente).filter(models.Cliente.id == id).first()

        if not cliente:
            raise HTTPException(status_code=404, detail=f"Cliente não encontrado.")

        try:
            db.session.delete(cliente)
            db.session.commit()
            return {
                "status": 200,
                "message": f"Cliente de número {id} excluído com sucesso!"
            }

        except Exception as error:
            db.session.rollback()
            raise HTTPException(status_code=500, detail=f"Não foi possível excluir o cliente. Detalhes: {str(error)}")