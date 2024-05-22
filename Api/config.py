import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:123456@localhost:5432/uriboca')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    @staticmethod
    def test_database_connection():
        engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        try:
            with engine.connect():
                print("Conexão bem-sucedida com o banco de dados!")
        except OperationalError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
