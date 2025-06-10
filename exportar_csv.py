import sqlite3
import pandas as pd

def gerar_csv():
    conn = sqlite3.connect('dados.db')
    df = pd.read_sql_query("SELECT * FROM transacoes", conn)
    df.to_csv("dados_financeiros.csv", index=False)
    conn.close()
