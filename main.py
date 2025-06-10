from ocr_extrator import extrair_dados_nota
from banco import init_db, inserir_transacao
from exportar_csv import gerar_csv

init_db()
nota_path = "image.png"

transacao = extrair_dados_nota(nota_path)
inserir_transacao(transacao)
gerar_csv()

print("Nota processada, transação salva e CSV atualizado!")
