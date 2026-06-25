from rich import print

from config import conexao, cursor

def excluirMarca():
    print("\n[bold red]Exclusão de Marca[/bold red]")

    id = input("ID da Marca: ")
    if not id.isdigit():
        print("[red]ID inválido. Digite um número inteiro.[/red]")
        return
    else:
        cursor.execute(
            """
            SELECT id, nome
            FROM marcas
            WHERE id = %s
            """,
            (id,),
        )
        marca = cursor.fetchone()

        if not marca:
            print("[red]Marca não encontrada[/red]")
            return

        print(
            f"[yellow]--->[/yellow][red]Deseja realmente excluir a marca {marca['nome']}?[/red]"
        )
        confirmacao = input("Digite Sim para confirmar ou qualquer outra tecla para cancelar: ")

        if confirmacao.lower() != "sim":
            print("[yellow]Exclusão cancelada.[/yellow]")
            return
