
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

def get_banco_key():
    conexao = psycopg2.connect(
            host="",
            dbname="",
            user="",
            password="",
            port="",
        )
    return conexao