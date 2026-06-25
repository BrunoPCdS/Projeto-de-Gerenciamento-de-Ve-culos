import plotly.express as px

from config import conexao, cursor

def gerar_grafico_veiculo(veiculos):
    # Cria um gráfico de barras usando Plotly Express
    cursor.execute(
        """
        SELECT v.modelo, COUNT(v.id) AS total_carros
        FROM veiculos v
        GROUP BY v.modelo
        ORDER BY total_carros DESC
        """,
    )
    veiculos = cursor.fetchall()

    fig = px.bar(
        veiculos, x="modelo", 
        y="total_carros", 
        labels={"modelo": "Modelo", "total_carros": "Total de Carros"},
        title="Total de Carros por Modelo")
    fig.show()