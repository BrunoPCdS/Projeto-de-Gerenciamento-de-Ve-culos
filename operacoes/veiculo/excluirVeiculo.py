from rich import print

from config import conexao, cursor


def excluirVeiculo():
    id = input("ID do veículo: ")
    if not id.isdigit():
        print("[red]ID inválido. Digite um número inteiro.[/red]")
        return
    else: 
        cursor.execute(
            """
            SELECT id, modelo, marca_id, ano, preco
            FROM veiculos
            WHERE id = %s
            """,
            (id,),
        )
        veiculo = cursor.fetchone()

        if not veiculo:
            print("[red]Veículo não encontrado[/red]")
            return

        print(
            f"[yellow]--->[/yellow][red]Deseja realmente excluir o veículo {veiculo['modelo']}?[/red]"
        )
        confirmacao = input("Digite Sim para confirmar ou qualquer outra tecla para cancelar: ")

        if confirmacao.lower() != "sim":
            print("[yellow]Exclusão cancelada.[/yellow]")
            return
