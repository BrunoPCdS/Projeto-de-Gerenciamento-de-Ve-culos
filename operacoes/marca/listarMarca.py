from rich import print
from rich.console import Console
from rich.table import Table

from config import conexao, cursor

def listarMarcas():
    print("\n[bold cyan]Lista de Marcas[/bold cyan]")

    cursor.execute(
        """
        SELECT m.id, m.nome, COUNT(v.id) AS total_carros
        FROM marcas m
        LEFT JOIN veiculos v ON m.id = v.marca_id
        GROUP BY m.id, m.nome
        ORDER BY m.id
        """,
    )
    marcas = cursor.fetchall()

    if not marcas:
        print("[yellow]Nenhuma marca cadastrada[/yellow]")
        return
    
    tabela = Table(title="Marcas Cadastradas")
    tabela.add_column("ID", justify="right")
    tabela.add_column("Nome", justify="left")
    tabela.add_column("Total de Carros", justify="right")

    for item in marcas:
        #print(f"[green]ID:[/green] {marca['id']} - [green]Nome:[/green] {marca['nome']}")
        tabela.add_row(
            str(item["id"]),
            item["nome"],
            str(item["total_carros"])
        )
    Console().print(tabela)