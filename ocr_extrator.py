import pytesseract
from PIL import Image
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extrair_dados_nota(caminho):
    imagem = Image.open(caminho)
    texto = pytesseract.image_to_string(imagem, lang='por')

    # Exemplos simples de extração
    valor = re.search(r'R\$\s?(\d+,\d{2})', texto)
    data = re.search(r'\d{2}/\d{2}/\d{4}', texto)

    return {
        "tipo": "despesa",
        "valor": float(valor.group(1).replace(',', '.')) if valor else 0.0,
        "data": data.group() if data else "00/00/0000",
        "categoria": "geral",
        "descricao": "Importado via nota",
        "origem": "nota",
        "nota_path": caminho
    }
