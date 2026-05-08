import numpy as np
from firebase_config import db
from fastapi import HTTPException
from services.calcular_agitador import get_dolar_bcb

def calcular_destilador_tray(material: str, tipo_bandeja: str, N:float, W:float, Tb:float, Tp:float, L:float, D:float) -> float:
    try:
        D = D * 3.28084  # Converter D de metros para pés
        L = L * 3.28084  # Converter L de metros para pés
        W = W * 2.20462  # Converter W de kg para lb
        # Obter os coeficientes do material
        doc_ref_material = db.collection("materiais_destilador").document(material)
        doc_material = doc_ref_material.get()

        if not doc_material.exists:
            raise HTTPException(status_code=404, detail="Material não encontrado no Firestore.")

        coef_material = doc_material.to_dict()
        f1 = coef_material["f1"]

        if material == "Aço Inoxidável, 304":
            f2 = 1.189 + (0.05770 * D)

        elif material == "Aço Inoxidável, 316":
            f2 = 1.401 + (0.07240 * D)
        
        elif material == "Carpenter 20CB-3":
            f2 = 1.525 + (0.07880 * D)

        elif material == "Monel - 400":
            f2 = 2.306 + (0.1120 * D)

        else:
            f2 = 1

        # Obter os coeficientes do tipo de tray
        doc_ref_tray = db.collection("tray_types_destilador").document(tipo_bandeja)
        doc_tray = doc_ref_tray.get()

        if not doc_tray.exists:
            raise HTTPException(status_code=404, detail="Tipo de tray não encontrado no Firestore.")

        coef_tray = doc_tray.to_dict()
        f3 = coef_tray["f3"]

        if N <= 20:
            f4 = 2.25/(1.0414 ** N)
        elif N > 20:
            f4 = 1

        log_w = np.log(W)
        log_w_squared = log_w**2
        log_tb_tp = np.log(Tb / Tp)
        l_d = L/D
        exponent = (7.123 + (0.1478 * log_w) + (0.02488 * log_w_squared) + (0.01580 * log_tb_tp * l_d))
        Cb = np.exp(exponent)


        exponent2 = 0.1739 * D
        Ct = (375.8 * np.exp(exponent2))


        Cp1 = (204.9 * (D ** 0.6332) * (L ** 0.8016))
        
        # Cálculo do preço
        preco1 = (f1 * Cb)
        preco2 = (N * f2 * f3 * f4 * Ct)
        preco_total = (preco1 + preco2 + Cp1)

        preco_reais = preco_total * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar o Firestore: {str(e)}")
    
def calcular_torre_absorcao_tray(material: str, tipo_bandeja: str, N:float, W:float, L:float, D:float) -> float:
    try:
        D = D * 3.28084  # Converter D de metros para pés
        L = L * 3.28084  # Converter L de metros para pés
        W = W * 2.20462  # Converter W de kg para lb
         # Obter os coeficientes do material
        doc_ref_material = db.collection("materiais_destilador").document(material)
        doc_material = doc_ref_material.get()

        if not doc_material.exists:
            raise HTTPException(status_code=404, detail="Material não encontrado no Firestore.")

        coef_material = doc_material.to_dict()
        f1 = coef_material["f1"]

        if material == "Aço Inoxidável, 304":
            f2 = 1.189 + (0.05770 * D)

        elif material == "Aço Inoxidável, 316":
            f2 = 1.401 + (0.07240 * D)
        
        elif material == "Carpenter 2OCB-3":
            f2 = 1.525 + (0.07880 * D)

        elif material == "Monel-400":
            f2 = 2.306 + (0.1120 * D)

        else:
            f2 = 1

        # Obter os coeficientes do tipo de tray
        doc_ref_tray = db.collection("tray_types_destilador").document(tipo_bandeja)
        doc_tray = doc_ref_tray.get()

        if not doc_tray.exists:
            raise HTTPException(status_code=404, detail="Tipo de tray não encontrado no Firestore.")

        coef_tray = doc_tray.to_dict()
        f3 = coef_tray["f3"]

        if N <= 20:
            f4 = 2.25/(1.0414 ** N)
        else:
            f4 = 1

        log_w = np.log(W)
        log_w_squared = log_w**2
        exponent = (6.629 + (0.1826 * log_w) + (0.02297 * log_w_squared))
        Cb = np.exp(exponent)
        
        exponent2 = 0.1739 * D
        Ct = (375.8 * np.exp(exponent2))

        Cp1 = (246.4 * (D ** 0.7396) * (L ** 0.7068))

        # Cálculo do preço
        preco1 = (f1 * Cb)
        preco2 = (N * f2 * f3 * f4 * Ct)
        preco_total = (preco1 + preco2 + Cp1)

        preco_reais = preco_total * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar o Firestore: {str(e)}")
    

def calcular_destilador_packed(material: str, W:float, Tb:float, Tp:float, L:float, D:float, V:float, tipo:str) -> float:
    try:
        D = D * 3.28084  # Converter D de metros para pés
        L = L * 3.28084  # Converter L de metros para pés
        W = W * 2.20462  # Converter W de kg para lb
        # Obter os coeficientes do material
        doc_ref_material = db.collection("materiais_destilador").document(material)
        doc_material = doc_ref_material.get()

        if not doc_material.exists:
            raise HTTPException(status_code=404, detail="Material não encontrado no Firestore.")

        coef_material = doc_material.to_dict()
        f1 = coef_material["f1"]


        log_w = np.log(W)
        log_w_squared = log_w**2
        log_tb_tp = np.log(Tb / Tp)
        l_d = L/D
        exponent = (7.123 + (0.1478 * log_w) + (0.02488 * log_w_squared) + (0.01580 * log_tb_tp * l_d))
        Cb = np.exp(exponent)


        
        doc_tipo_empacotamento = db.collection("tipo_empacotamento").document(tipo)
        doc_tipo = doc_tipo_empacotamento.get()

        if not doc_material.exists:
            raise HTTPException(status_code=404, detail="Material não encontrado no Firestore.")
        
        coef_tipo = doc_tipo.to_dict()
        Cp = coef_tipo["Cp"]


        Cp1 = (204.9 * (D ** 0.6332) * (L ** 0.8016))
        
        # Cálculo do preço
        preco1 = (f1 * Cb)
        preco2 = (V * Cp)
        preco_total = (preco1 + preco2 + Cp1)

        preco_reais = preco_total * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar o Firestore: {str(e)}")
    
def calcular_torre_absorcao_packed(material: str, W:float, L:float, D:float, V:float, tipo:str) -> float:
    try:
        D = D * 3.28084  # Converter D de metros para pés
        L = L * 3.28084  # Converter L de metros para pés
        W = W * 2.20462  # Converter W de kg para lb
         # Obter os coeficientes do material
        doc_ref_material = db.collection("materiais_destilador").document(material)
        doc_material = doc_ref_material.get()

        if not doc_material.exists:
            raise HTTPException(status_code=404, detail="Material não encontrado no Firestore.")

        coef_material = doc_material.to_dict()
        f1 = coef_material["f1"]

        log_w = np.log(W)
        log_w_squared = log_w**2
        exponent = (6.629 + (0.1826 * log_w) + (0.02297 * log_w_squared))
        Cb = np.exp(exponent)

        doc_tipo_empacotamento = db.collection("tipo_empacotamento").document(tipo)
        doc_tipo = doc_tipo_empacotamento.get()

        if not doc_material.exists:
            raise HTTPException(status_code=404, detail="Material não encontrado no Firestore.")
        
        coef_tipo = doc_tipo.to_dict()
        Cp = coef_tipo["Cp"]

        Cp1 = (246.4 * (D ** 0.7396) * (L ** 0.7068))

       # Cálculo do preço
        preco1 = (f1 * Cb)
        preco2 = (V * Cp)
        preco_total = (preco1 + preco2 + Cp1)

        preco_reais = preco_total * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar o Firestore: {str(e)}")