from rich.console import Console
from rich.table import Table

from config import cursor


def listarVeiculos():
    if cursor.execute("SELECT COUNT(*) AS total FROM veiculos") and cursor.fetchone()["total"] == 0:
        print("[yellow]--->[/yellow][red]Não há veículos cadastrados.[/red]")
        return
    
    cursor.execute(
        """
        SELECT v.id, v.modelo, m.nome AS marca, v.ano, v.preco
        FROM veiculos v
        INNER JOIN marcas m ON v.marca_id = m.id
        ORDER BY m.nome, v.modelo
        """
    )
    dados = cursor.fetchall()

    tabela = Table(title="Veículos Cadastrados")
    tabela.add_column("ID", justify="right")
    tabela.add_column("Modelo")
    tabela.add_column("Marca")
    tabela.add_column("Ano")
    tabela.add_column("Preço", justify="right")

    for item in dados:
        tabela.add_row(
            str(item["id"]),
            item["modelo"],
            item["marca"],
            str(item["ano"]),
            f'R$ {float(item["preco"]):.2f}',
        )

    Console().print(tabela)