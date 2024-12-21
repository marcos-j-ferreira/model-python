from dotenv import load_dotenv
import os
import psycopg2 

load_dotenv()

# config of database
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# function for connect with database
def log ():

    try:

        connection = psycopg2.connect(
            user = db_user,
            host = db_host,
            dbname = db_name,
            password = db_password,
            port = db_port
        )

        cursor = connection.cursor()

        print("\n -- conexão estabelecida --\n")

        return connection

    except Exception as e:
        print(f"\n Erro ao conectar ao banco de dados \n Erro: {e}")
        return None
