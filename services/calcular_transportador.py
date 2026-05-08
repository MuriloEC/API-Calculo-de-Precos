from services.calcular_agitador import get_dolar_bcb
import numpy as np


def metros_para_pes(metros):
    return (metros * 3.28084)

def kg_hr_para_klb_hr(kg_hr):
    return kg_hr * 0.00220462

def calcular_transportadora(comprimento: int, tipo: str, vazao: int) -> float:
    vazao_massica_Klb = kg_hr_para_klb_hr(vazao)
    comprimento_pes = metros_para_pes(comprimento)
    if(tipo == "Transportador de Correia com Calha"):
        pot = (comprimento_pes ** 0.66)
        preco = (pot * 1.40) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Transportador de Correia Plana"):
        pot = (comprimento_pes ** 0.66)
        preco = (pot * 0.90) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Transportador Helicoidal de Aço"):
        pot = (comprimento_pes ** 0.78)
        preco = (pot * 0.40) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Transportador Helicoidal de Aço Inoxidável"):
        pot = (comprimento_pes ** 0.78)
        preco = (pot * 0.70) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Transportador de Correia com Caçambas"):
        pot = (comprimento_pes ** 0.63)
        preco = (pot * 4.22) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Transportador Pneumático"):
        log_W = np.log(vazao_massica_Klb)
        log_W_squared = (log_W**2)
        exponent = (3.5612 - (0.0048 * log_W) + (0.0913 * log_W_squared))
        preco = np.exp(exponent) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")