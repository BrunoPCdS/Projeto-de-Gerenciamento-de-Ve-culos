from rich import print

from config import conexao, cursor
from operacoes.marca.selecionarMarca import selecionarMarca


def incluirVeiculo():
    while True:
        marca_id = selecionarMarca("Marca")
        if marca_id is None:
            input("Pressione Enter para voltar...")
            return

        print("\nDigite [red] Exit [/red] para voltar ao menu.")

        nome = input("Modelo.................: ").strip()

        if nome == "Exit" or nome == "exit":
            return

        try:
            ano = int(input("Ano....................: ").strip())
            valor = float(input("Preço R$...............: ").strip())
        except ValueError:
            print("[red]Digite apenas valores válidos.[/red]")
            continue

        foto = input("Foto (URL ou caminho)...: ").strip()

        if valor < 0:
            print("[red]O preço deve ser positivo.[/red]")
            continue

        cursor.execute(
            """
            INSERT INTO veiculos (marca_id, modelo, ano, preco, foto)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (marca_id, nome, ano, valor, foto),
        )

        conexao.commit()

        print("[green]Veículo cadastrado com sucesso![/green]")

        opcao = input(
            "\nDigite Sim para cadastrar outro veículo ou Exit para voltar: "
        ).strip()

        if opcao == "exit" or opcao == "Exit":
            return