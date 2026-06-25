from flask import Flask, render_template
from config import cursor

app = Flask(__name__)

@app.route('/')
def index():
    cursor.execute(
        """
        SELECT v.id, v.modelo, m.nome AS marca, v.ano, v.preco, v.foto
        FROM veiculos v
        INNER JOIN marcas m ON v.marca_id = m.id
        ORDER BY m.nome, v.modelo
        """
    )
    veiculos = cursor.fetchall()
    return render_template('index.html', veiculos=veiculos)

if __name__ == '__main__':
    app.run(debug=True)
