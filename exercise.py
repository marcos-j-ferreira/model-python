from dotenv import load_dotenv
import psycopg2 
import os 

load_dotenv()
db_nome = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

class Model: 

    def __init__():
        self.unknown = "Unknown"

    def log():

        try:
            connection = psycopg2.connect(
                dbname = db_nome,
                user = db_user,
                password =  db_password,
                host = db_host,
                port = db_port
            )
            cursor = connection.cursor()
            print("\n -- conexão estabelecida -- \n")
            return connection
        
        except Exception as e:
            print(f"\n -- Erro ao conectar ao banco de dados \n Erro:{e}")
            return None

model = Model.log()