from rich import print
from rich.prompt import Prompt

from config import cursor


def selecionarMarca(titulo="Marca", marca_atual=None):
    cursor.execute(
        """
        SELECT id, nome
        FROM marcas
        ORDER BY id
        """
    )
    marcas = cursor.fetchall()

    if not marcas:
        print("[red]Não há marcas cadastradas.[/red]")
        return None

    print("\n[bold cyan]Marcas cadastradas[/bold cyan]")
    for marca in marcas:
        print(f"[green]ID:[/green] {marca['id']} - [green]Nome:[/green] {marca['nome']}")

    choices = [str(marca["id"]) for marca in marcas]
    default = str(marca_atual) if marca_atual is not None else choices[0]

    return int(
        Prompt.ask(
            f"{titulo} (escolha o ID)",
            choices=choices,
            default=default,
        )
    )