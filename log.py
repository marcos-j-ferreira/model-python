from dotenv import load_dotenv
import os
import psycopg2 

load_dotenv()

db_name = os.getenv("DB_NAME")


print(db_name)

