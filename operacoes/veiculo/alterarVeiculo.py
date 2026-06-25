from rich import print

from config import conexao, cursor
from operacoes.marca.selecionarMarca import selecionarMarca


def alterarVeiculo():
    id = input("ID do veículo: ")
    
    if not id.isdigit():
        print("[red]ID inválido. Digite um número inteiro.[/red]")
        return

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

    print("\n[bold yellow]Alteração[/bold yellow]")

    modelo = input(f"Modelo [{veiculo['modelo']}]: ").strip() or veiculo["modelo"]
    marca_id = selecionarMarca("Marca", veiculo["marca_id"])
    if marca_id is None:
        return
    ano = input(f"Ano [{veiculo['ano']}]: ").strip() or veiculo["ano"]
    preco = input(f"Preço [{float(veiculo['preco']):.2f}]: ").strip() or veiculo["preco"]

    if float(preco) < 1:
        print("[red]O valor mínimo do veículo é R$ 1,00.[/red]")
        return

    cursor.execute(
        """
        UPDATE veiculos
        SET modelo = %s, marca_id = %s, ano = %s, preco = %s
        WHERE id = %s
        """,
        (modelo, marca_id, ano, preco, id),
    )
    conexao.commit()

    print("[green]Veículo alterado![/green]")