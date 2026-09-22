from datetime import datetime, timedelta
from db.connection import DBConnection
from db import models

def calculo_preco_validacao_horario(dados_inicio: datetime, dados_final: datetime) -> float:

    if dados_inicio > dados_final:
            raise ValueError ("O horário final deve ser depois do horário inicial")
        
    if dados_inicio < (datetime.now() + timedelta(hours=2)):
            raise ValueError ("Você só pode marcar duas horas depois do horário atual")



    hora_inicio = dados_inicio.hour    

    if hora_inicio < 8:
        raise ValueError("O horário de funcionamento é das 8h as 23:59")


    dia_semana = dados_inicio.weekday()
    valor_hora = None

    if dia_semana < 5:
            valor_hora = 80.00 if hora_inicio < 18 else 120.00

    else:
        valor_hora = 120.00


    # preço
    duracao_segundos = (dados_final - dados_inicio).total_seconds()
    duracao_hora = duracao_segundos / 3600

    # checagem do tempo de jogo
    if duracao_hora < 1:
        raise ValueError("O tempo mínimo de jogo é 1h!")

    preco = valor_hora * duracao_hora
    return preco

def verifica_choque(db: DBConnection, dados_inicio: datetime, dados_final: datetime, agendamento_id: int = None) -> None:
    pesquisa = db.session.query(models.Agendamento).filter(
        models.Agendamento.data_hora_inicio < dados_final,
        models.Agendamento.data_hora_final > dados_inicio 
        )

    # caso de atualização
    if agendamento_id:
        pesquisa = pesquisa.filter(models.Agendamento.id != agendamento_id)

    choque = pesquisa.first()
    
    if choque:
        raise ValueError("A quadra já está ocupada neste horário")
     