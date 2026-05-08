import requests
import numpy as np
from firebase_config import db
from fastapi import HTTPException
from services.calcular_agitador import get_dolar_bcb
import locale



def calcular_compressor(hp: int, tipo: str) -> float:
    if(tipo == "Compressor Centrífugo (Sem Acionador)"):
        potencia = 0.62
        multiplicacao = 6.49

    elif(tipo == "Compressor Alternativo (Sem Acionador)"):
        potencia = 0.61
        multiplicacao = 5.96

    elif(tipo == "Compressor Parafuso (Com Acionador)"):
        potencia = 0.71
        multiplicacao = 1.49

    
    pot = (hp ** potencia)
    preco = (pot * multiplicacao) * 1000
    preco_reais = preco * get_dolar_bcb()
    return "{:.2f}".format(preco_reais).replace(".", ",")

def calcular_turbina(hp: int, tipo: str) -> float:
    if(tipo == "Turbina de Descarga por Pressão"):
        multiplicacao = 0.31

    elif(tipo == "Turbina de Descarga a Vácuo"):
        multiplicacao = 0.69

    pot = (hp ** 0.81)
    preco = (pot * multiplicacao) * 1000
    preco_reais = preco * get_dolar_bcb()
    return "{:.2f}".format(preco_reais).replace(".", ",")

'''def calcular_ventilador(tipo: str, material: str, pressao: int, vazao: float) -> float:
    try:
        doc_ref = db.collection("coeficientes_fans").document(tipo)
        doc_ref_fm = db.collection("fatores_materiais").document(material)
        doc_ref_fp = db.collection("fatores_pressao").document(tipo).collection(pressao).document()
        doc = doc_ref.get()
        doc_fm = doc_ref_fm.get()
        doc_fp = doc_ref_fp.get()


        if not doc.exists:
            raise HTTPException(status_code=404, detail="Parâmetros não encontrados no Firestore.")

        coef = doc.to_dict()
        a = coef["a"]
        b = coef["b"]
        c = coef["c"]

        coef_fm = doc_fm.to_dict()
        fm = coef_fm["fator_m"]

        coef_fp = doc_fp.to_dict()
        fp = coef_fp["fp"]


        log_vazao = np.log(vazao)
        log_vazao_squared = log_vazao**2
        exponent = (a + (b * log_vazao) + (c * log_vazao_squared))
        preco = np.exp(exponent)
        preco_reais = preco * get_dolar_bcb()
        preco_formatado = locale.currency(preco_reais, grouping=True, symbol=False)
        return preco_formatado

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar o Firestore: {str(e)}")'''