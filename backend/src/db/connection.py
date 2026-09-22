import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

Base = declarative_base()

class DBConnection:
    def __init__(self) -> None:
        dialect = os.getenv("DB_DIALECT", "postgresql")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "5432")
        database = os.getenv("DB_NAME")
        
        self.__connection_string = f"{dialect}://{user}:{password}@{host}:{port}/{database}"
        
        # Cria o motor
        self.__engine = self.__create_database_engine()
        
        # Cria a fábrica de sessões UMA Ú   NICA VEZ
        self.__session_maker = sessionmaker(bind=self.__engine)

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    # Entrada e saída para o 'with'
    def __enter__(self):
        # Apenas pede para a fábrica criar uma nova sessão
        self.session = self.__session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Garante que a sessão seja fechada sempre
        self.session.close()