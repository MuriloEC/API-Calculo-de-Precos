import numpy as np
import requests
from firebase_config import db
from fastapi import HTTPException
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def get_dolar_bcb():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json"
    response = requests.get(url)
    data = response.json()
    valor = data[0]['valor']
    return float(valor.replace(",", "."))


    
def get_faixa_velocidade(velocidade: float) -> str:
    if velocidade <= 45:
        return "Baixa"
    elif 56 <= velocidade <= 100:
        return "Média"
    elif 125 <= velocidade <= 230:
        return "Alta"
    else:
        return "Indefinida"

def calcular_agitador(tipo: str, material: str, velocidade: float, hp: int) -> float:
    faixa = get_faixa_velocidade(velocidade)

    if faixa == "Indefinida":
        raise HTTPException(status_code=400, detail="Velocidade fora da faixa suportada.")

    try:
        doc_ref = db.collection("coeficientes").document(tipo).collection(material).document(faixa)
        doc = doc_ref.get()

        if not doc.exists:
            raise HTTPException(status_code=404, detail="Parâmetros não encontrados no Firestore.")

        coef = doc.to_dict()
        a = coef["a"]
        b = coef["b"]
        c = coef["c"]

        log_HP = np.log(hp)
        log_HP_squared = log_HP**2
        exponent = (a + (b * log_HP) + (c * log_HP_squared))
        preco = np.exp(exponent)
        preco_reais = preco * get_dolar_bcb()
        preco_formatado = locale.currency(preco_reais, grouping=True, symbol=False)
        return preco_formatado

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar o Firestore: {str(e)}")
    
    




