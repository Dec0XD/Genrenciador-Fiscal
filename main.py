from ocr_extrator import extrair_dados_nota
from banco import init_db, inserir_transacao
from exportar_csv import gerar_csv
import sqlite3

def nota_ja_processada(nota_path):
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM transacoes WHERE nota_path = ?", (nota_path,))
    existe = c.fetchone()[0] > 0
    conn.close()
    return existe

init_db()
nota_path = "image.png"

if not nota_ja_processada(nota_path):
    transacao = extrair_dados_nota(nota_path)
    inserir_transacao(transacao)
    gerar_csv()
    print("Nota processada, transação salva e CSV atualizado!")
else:
    print("Nota já processada anteriormente.")
