
from psycopg2.extras import RealDictCursor
import psycopg2
from operacoes.banco.bancoKey import get_banco_key



conexao = get_banco_key()

cursor = conexao.cursor(cursor_factory=RealDictCursor)

print("Conexão bem-sucedida!")


def inicializar_banco():

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marcas (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(120) NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS veiculos (
            id SERIAL PRIMARY KEY,
            modelo VARCHAR(120) NOT NULL,
            ano INTEGER NOT NULL,
            preco NUMERIC(10,2) NOT NULL CHECK (preco >= 0),
            foto VARCHAR(500) NOT NULL,
                   
            marca_id INTEGER NOT NULL,
            FOREIGN KEY (marca_id) REFERENCES marcas(id)
        )
    """)

    conexao.commit()
