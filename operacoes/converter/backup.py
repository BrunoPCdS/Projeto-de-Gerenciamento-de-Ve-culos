import csv
from psycopg2.extras import RealDictCursor
from datetime import datetime
from operacoes.banco.bancoKey import get_banco_key

def backup_veiculos():
    # Inicializa as variáveis para garantir que o bloco 'finally' consiga fechá-las
    conexao = None
    cursor = None
    
    try:
        
        conexao = get_banco_key()

        cursor = conexao.cursor(cursor_factory=RealDictCursor)

        cursor.execute("SELECT * FROM veiculos")
        veiculos = cursor.fetchall()  

        if not veiculos:
            print("Nenhum veículo encontrado na tabela.")
            return 
            
        # Definindo as colunas exatas que você quer no CSV
        colunas = ['id', 'modelo', 'ano', 'preco', 'foto', 'marca_id']

        # Gerando o nome do arquivo (opcional: você pode fixar apenas 'backup_veiculos.csv')
        # Adicionar o timestamp evita que um backup apague o anterior
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"backup_veiculos_{timestamp}.csv"

        # Abre o arquivo para escrita
        # Usamos o delimitador ';' porque o Excel em português reconhece melhor as colunas
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=';')
            
            # Escreve o cabeçalho automaticamente baseado na lista 'colunas'
            writer.writeheader()  

            # Como 'veiculos' já é uma lista de dicionários, o DictWriter consegue 
            # escrever todas as linhas de uma vez só, sem precisar do laço 'for'!
            writer.writerows(veiculos)

        print(f"Backup dos veículos realizado com sucesso! Arquivo: {nome_arquivo}")

    except Exception as e:
        print(f"Ocorreu um erro ao realizar o backup: {e}")
        
    finally:
        # Garante que as conexões com o Neon sejam fechadas corretamente
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()