from rich import print

from config import conexao, cursor

def incluirMarca():
    print("\n[bold green]Inclusão de Marca[/bold green]")

    nome = input("Nome da Marca........: ").strip()
    if not nome:
        print("[red]O nome da marca não pode ser vazio.[/red]")
        return

    cursor.execute(
        """
        INSERT INTO marcas (nome)
        VALUES (%s)
        """,
        (nome,),
    )
    conexao.commit()

    print("[green]Marca cadastrada com sucesso![/green]")