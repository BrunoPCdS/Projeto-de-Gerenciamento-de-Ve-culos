from rich.console import Console
from rich.panel import Panel
import subprocess
import webbrowser
import time

from config import inicializar_banco
from operacoes.veiculo.incluirVeiculo import incluirVeiculo
from operacoes.veiculo.listarVeiculo import listarVeiculos
from operacoes.veiculo.alterarVeiculo import alterarVeiculo
from operacoes.veiculo.excluirVeiculo import excluirVeiculo
from operacoes.marca.incluirMarca import incluirMarca
from operacoes.marca.listarMarca import listarMarcas
from operacoes.marca.excluirMarca import excluirMarca
from operacoes.tabelaMarcas import gerar_grafico_marca
from operacoes.tabelaVeiculos import gerar_grafico_veiculo

console = Console()

menu = ("""
1. Incluir veículo
2. Listar veículos
3. Alterar veículo
4. [green]Gerar gráfico de veículos[/green]
5. [red]Excluir veículo[/red]
6. Incluir marca
7. Listar marcas
8. [green]Gerar gráfico de marcas[/green]
9. [red]Excluir marca[/red]
10. [blue]Abrir visualização na Web[/blue]
11. [green]Gerar backup de veículos[/green]
12. [yellow]Finalizar[/yellow]
""")


inicializar_banco()

while True:
    console.clear()
    console.print(Panel.fit(menu, title="Menu Principal"))

    try:
        opcao = int(input("Opção: "))
    except ValueError:
        console.print("[bold red]Digite uma opção válida![/bold red]")
        input("\nPressione Enter para continuar...")
        continue

    if opcao == 1:
        incluirVeiculo()
    elif opcao == 2:
        listarVeiculos()
    elif opcao == 3:
        alterarVeiculo()
    elif opcao == 4:
        gerar_grafico_veiculo(listarVeiculos())
    elif opcao == 5:
        excluirVeiculo()
    elif opcao == 6:
        incluirMarca()
    elif opcao == 7:
        listarMarcas()
    elif opcao == 8:
        gerar_grafico_marca(listarMarcas())
    elif opcao == 9:
        excluirMarca()
    elif opcao == 10:
        console.print("Abrindo a visualização na web...")
        subprocess.Popen(["python", "app.py"])
        time.sleep(2)  # Dá um tempo para o servidor iniciar
        webbrowser.open_new_tab("http://127.0.0.1:5000")
    elif opcao == 11:
        from operacoes.converter.backup import backup_veiculos
        backup_veiculos()
    elif opcao == 12:
        console.print("[bold cyan]Fim do Programa[/bold cyan]")
        break

    else:
        console.print("[bold red]Opção inválida[/bold red]")

    input("\nPressione Enter para continuar...")