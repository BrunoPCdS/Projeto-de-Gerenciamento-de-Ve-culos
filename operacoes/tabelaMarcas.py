import plotly.express as px

from config import conexao, cursor

def gerar_grafico_marca(marcas):
    # Cria um gráfico de barras usando Plotly Express
    cursor.execute(
        """
        SELECT m.nome, COUNT(v.id) AS total_carros
        FROM marcas m
        LEFT JOIN veiculos v ON m.id = v.marca_id
        GROUP BY m.nome
        ORDER BY total_carros DESC
        """,
    )
    marcas = cursor.fetchall()

    fig = px.bar(
        marcas, x="nome", 
        y="total_carros", 
        labels={"nome": "Marca", "total_carros": "Total de Carros"},
        title="Total de Carros por Marca")
    fig.show()
