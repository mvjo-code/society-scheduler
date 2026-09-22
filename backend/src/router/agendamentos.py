from fastapi import APIRouter, HTTPException, Depends
from db.connection import DBConnection
import schemas
from db import models
from utils import utils_agendamento_route
from utils import security

router =  APIRouter(prefix="/agendamento", tags=["agendamentos"])

@router.get("/meus", response_model=list[schemas.AgendamentoResponse])
def listar_meus_agendamentos(email_cliente: str = Depends(security.obter_usuario_atual)):
    '''retorna só os agendamentos do cliente logado'''
    try:
        with DBConnection() as db:
            cliente = db.session.query(models.Cliente).filter(models.Cliente.email == email_cliente).first()

            if not cliente:
                raise HTTPException(status_code=404, detail="Cliente não encontrado.")

            agendamentos = db.session.query(models.Agendamento).filter(
                models.Agendamento.id_cliente == cliente.id
            ).all()

            return agendamentos

    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar agendamentos. Detalhes: {str(error)}")



@router.get("/", response_model=list[schemas.AgendamentoResponse])
def listar_agendamentos():
    '''funcao para listar agendamentos'''
    try:
        with DBConnection() as db:
            
            todos_os_agendamentos = db.session.query(models.Agendamento).all()

            return todos_os_agendamentos
        
    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Não foi possível fazer a busca no banco de dados. Detalhes: {str(error)}"
        )

@router.post("/", response_model=schemas.AgendamentoResponse)
def agendar(dados_agendamento: schemas.AgendamentoCreate,
            email_cliente: str = Depends(security.obter_usuario_atual)
                ):


    # regras iniciais para agendamento
    try:
        preco_calculado = utils_agendamento_route.calculo_preco_validacao_horario(dados_agendamento.data_hora_inicio, dados_agendamento.data_hora_final)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
    

    # sessão
    with DBConnection() as db:

        cliente_existe = db.session.query(models.Cliente).filter(models.Cliente.email == email_cliente).first()

        if not cliente_existe:
            raise HTTPException (status_code=404, detail="Cliente não encontrado no sistema")

        id_cliente = cliente_existe.id

        try:
            utils_agendamento_route.verifica_choque(db, dados_agendamento.data_hora_inicio, dados_agendamento.data_hora_final)

        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"{str(e)}")
        
        # criando modelo de agendamento
        novo_agendamento = models.Agendamento(
            id_cliente=id_cliente,
            data_hora_inicio=dados_agendamento.data_hora_inicio,
            data_hora_final=dados_agendamento.data_hora_final,
            preco=preco_calculado,
            status=dados_agendamento.status
        )

        try:
            db.session.add(novo_agendamento)
            db.session.commit()
            db.session.refresh(novo_agendamento)

            return novo_agendamento

        except Exception as error:
            db.session.rollback()

            raise HTTPException(status_code=500, detail=f"Não foi possível savar o agendamento. Detalhes: {str(error)}")

@router.put("/{id}", response_model=schemas.AgendamentoResponse)
def alterar_agendamento(id: int, dados_novos: schemas.AgendamentoCreate,
                        email_cliente: str = Depends(security.obter_usuario_atual)
                        ):

    # regras iniciais para agendamento
    try:
        preco_calculado = utils_agendamento_route.calculo_preco_validacao_horario(dados_novos.data_hora_inicio, dados_novos.data_hora_final)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")

    #session
    with DBConnection() as db:
        jogo = db.session.query(models.Agendamento).filter(models.Agendamento.id == id).first()
        cliente = db.session.query(models.Cliente).filter(models.Cliente.email == email_cliente).first()

        if not jogo:
            raise HTTPException(status_code= 404, detail=f"O jogo de número {id} não existe.")

        #verifica se tem choque do horário para o novo agendamento
        try:
            utils_agendamento_route.verifica_choque(db, dados_novos.data_hora_inicio, dados_novos.data_hora_final, id)

        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

        # atualizando agendamento
        jogo.data_hora_inicio = dados_novos.data_hora_inicio
        jogo.data_hora_final = dados_novos.data_hora_final
        jogo.id_cliente = cliente.id
        jogo.preco = preco_calculado
        jogo.status = dados_novos.status

        try:
            db.session.commit()
            db.session.refresh(jogo)

            return jogo

        except Exception as error:
            db.session.rollback()
            raise HTTPException(status_code=500, detail=f"Erro na conexão com o banco. Detalhes: {str(error)}")


@router.delete("/{id}")
def cancelar_agendamento(id: int):

    with DBConnection() as db:
        jogo = db.session.query(models.Agendamento).filter(models.Agendamento.id == id).first()

        if not jogo:
            raise HTTPException(status_code=404, detail=f"Agendamento não encontrado")

        try:
            db.session.delete(jogo)
            db.session.commit()
            return {
                "status": 200,  
                "message": f"Agendamento de número {id} cancelado com sucesso!"
            }

        except Exception as error:
            db.session.rollback()
            raise HTTPException(status_code=500, detail=f"Erro ao tentar excluir agendamento. Detalhes: {str(error)}")
