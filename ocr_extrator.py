import pytesseract
from PIL import Image
import re
import cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(caminho):
    imagem = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    imagem = cv2.resize(imagem, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    _, imagem = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return Image.fromarray(imagem)

def extrair_dados_nota(caminho):
    imagem = preprocess_image(caminho)
    texto = pytesseract.image_to_string(imagem, lang='por', config='--psm 6')
    print(texto)

    # Regex para capturar o valor total da nota (linha específica)
    match = re.search(r'VALOR\s+TOTAL\s+DA\s+NOTA.*?(\d{1,3}(?:[.\s]?\d{3})*,\d{2})', texto, re.DOTALL | re.IGNORECASE)
    valor_float = 0.0
    if match:
        valor_str = match.group(1)
        valor_float = float(valor_str.replace('.', '').replace(' ', '').replace(',', '.'))
    else:
        # fallback: pega o maior valor monetário encontrado
        valores = re.findall(r'(\d{1,3}(?:[.\s]?\d{3})*,\d{2})', texto)
        if valores:
            valores_float = [
                float(v.replace('.', '').replace(' ', '').replace(',', '.'))
                for v in valores
            ]
            valor_float = max(valores_float)

    data = re.search(r'\d{2}/\d{2}/\d{4}', texto)

    return {
        "tipo": "despesa",
        "valor": valor_float,
        "data": data.group() if data else "00/00/0000",
        "categoria": "geral",
        "descricao": "Importado via nota",
        "origem": "nota",
        "nota_path": caminho
    }
