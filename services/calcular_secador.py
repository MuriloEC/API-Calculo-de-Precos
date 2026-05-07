import numpy as np
from firebase_config import db
from fastapi import HTTPException
from services.calcular_agitador import get_dolar_bcb

def calcular_secador_rotary_combustion_gas_heated(material:str, tipo_gas:str, area:float):
    try:
        area = area * 10.7639  # Converter m² para ft²
        # Obter os coeficientes do material
        doc_ref_material = db.collection("Material_Dryer").document(material)
        doc_material = doc_ref_material.get()

        if not doc_material.exists:
            raise HTTPException(status_code=404, detail="Material não encontrado no Firestore.")

        coef_material = doc_material.to_dict()
        fm = coef_material["value"]

        # Obter os coeficientes do tipo de gás de secagem
        doc_ref_gas = db.collection("DryingGas_Dryer").document(tipo_gas)
        doc_gas = doc_ref_gas.get()

        if not doc_gas.exists:
            raise HTTPException(status_code=404, detail="Tipo de gás de secagem não encontrado no Firestore.")

        coef_gas = doc_gas.to_dict()
        fg = coef_gas["value"]

        # Cálculo do custo do secador rotativo aquecido a gás de combustão
        ln_A = np.log(area)
        ln_A_squared = ln_A**2
        expoente = (4.9504 - (0.5827 * ln_A) + (0.0925 * ln_A_squared))
        calc_expo = np.exp(expoente)
        c = (1 + fg + fm) * calc_expo


        # Conversão para reais
        dolar_bcb = get_dolar_bcb()
        C_reais = c * dolar_bcb

        return "{:.2f}".format(C_reais).replace(".", ",")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def calcular_secador_hot_air_heated(material:str, tipo_gas:str, area:float):
    try:
        area = area * 10.7639  # Converter m² para ft²
        # Obter os coeficientes do material
        doc_ref_material = db.collection("Material_Dryer").document(material)
        doc_material = doc_ref_material.get()

        if not doc_material.exists:
            raise HTTPException(status_code=404, detail="Material não encontrado no Firestore.")

        coef_material = doc_material.to_dict()
        fm = coef_material["value"]

        # Obter os coeficientes do tipo de gás de secagem
        doc_ref_gas = db.collection("DryingGas_Dryer").document(tipo_gas)
        doc_gas = doc_ref_gas.get()

        if not doc_gas.exists:
            raise HTTPException(status_code=404, detail="Tipo de gás de secagem não encontrado no Firestore.")

        coef_gas = doc_gas.to_dict()
        fg = coef_gas["value"]

        # Cálculo do custo do secador rotativo aquecido a gás de combustão
        A = area**0.63      
        C = 2.38 * (1 + fg + fm) * A


        # Conversão para reais
        dolar_bcb = get_dolar_bcb()
        C_reais = C * dolar_bcb

        return "{:.2f}".format(C_reais).replace(".", ",")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def calcular_secador_rotary_steam_tube(material:str, area:float):
    if material == "Aço Carbono":
        f = 1
    elif material == "Aço Inoxidável, 304":
        f = 1.75
    

    area = area * 10.7639  # Converter m² para ft²
    A = area**0.60
    C = 1.83 * f * A

    dolar_bcb = get_dolar_bcb()
    C_reais = C * dolar_bcb

    return "{:.2f}".format(C_reais).replace(".", ",")

def calcular_secador_cabinet_dryer(tipo_pressao:str, area:float):
    try:
        area = area * 10.7639  # Converter m² para ft²
        # Obter os coeficientes do material
        doc_ref_pressao = db.collection("Pressure_Dryer").document(tipo_pressao)
        doc_pressao = doc_ref_pressao.get()

        if not doc_pressao.exists:
            raise HTTPException(status_code=404, detail="Material não encontrado no Firestore.")

        coef_material = doc_pressao.to_dict()
        fp = coef_material["value"]

        # Cálculo do custo do secador rotativo aquecido a gás de combustão
        A = area**0.77     
        C = 1.15 * fp * A


        # Conversão para reais
        dolar_bcb = get_dolar_bcb()
        C_reais = C * dolar_bcb

        return "{:.2f}".format(C_reais).replace(".", ",")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    

def calcular_secador_spray_dryer(material:str, vazao:float):
    try:
        vazao = vazao * 2.20462  # Converter kg para lb
        # Obter os coeficientes do material
        doc_ref_material = db.collection("Material_Spray_Dryer").document(material)
        doc_material = doc_ref_material.get()

        if not doc_material.exists:
            raise HTTPException(status_code=404, detail="Material não encontrado no Firestore.")

        coef_material = doc_material.to_dict()
        f = coef_material["value"]

        
        ln_x = np.log(vazao)
        ln_x_squared = ln_x**2
        expoente = (0.8403 + (0.8526 * ln_x) - (0.0229 * ln_x_squared))
        C = f * np.exp(expoente)
        


        # Conversão para reais
        dolar_bcb = get_dolar_bcb()
        C_reais = C * dolar_bcb

        return "{:.2f}".format(C_reais).replace(".", ",")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def calcular_secador_multiple_hearth_furnaces(n_lareira: int, diametro: str):

    if diametro == '6':
        a = 5.071
    elif diametro == '10':
        a = 5.295
    elif diametro == '14.25':
        a = 5.521
    elif diametro == '16.75':
        a = 5.719
    elif diametro == '18.75':
        a = 5.853
    elif diametro == '22.25':
        a = 6.014
    elif diametro == '26.75':
        a = 6.094

    
    aux = (0.88 * n_lareira)
    expoente = (a + aux)
    C = np.exp(expoente)
        


    # Conversão para reais
    dolar_bcb = get_dolar_bcb()
    C_reais = C * dolar_bcb

    return "{:.2f}".format(C_reais).replace(".", ",")
