import streamlit as st
from banco import init_db, inserir_transacao
from ocr_extrator import extrair_dados_nota
from exportar_csv import gerar_csv
import tempfile
import os

st.title("Gerenciador Fiscal")

init_db()

st.header("Envio de Notas Fiscais")
uploaded_files = st.file_uploader(
    "Selecione uma ou mais notas fiscais (imagens, PDF ou XML):",
    type=["pdf", "xml", "png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        # Salva arquivo temporariamente
        suffix = os.path.splitext(file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
            tmp_file.write(file.read())
            tmp_path = tmp_file.name

        # Extrai dados e insere no banco
        transacao = extrair_dados_nota(tmp_path)
        inserir_transacao(transacao)
        st.success(f"Nota '{file.name}' processada e salva.")

    gerar_csv()
    st.info("CSV atualizado com as novas transações.")

st.write("Faça upload de suas notas fiscais para processar e salvar automaticamente.")
