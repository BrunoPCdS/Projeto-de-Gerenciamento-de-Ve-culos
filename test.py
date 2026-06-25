from config import inicializar_banco, cursor

inicializar_banco()
cursor.execute("SELECT COUNT(*) AS total FROM veiculos")
print(f"Tabela veiculos pronta. Registros: {cursor.fetchone()['total']}")
