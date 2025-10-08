from services.calcular_agitador import get_dolar_bcb


def m3h_para_kgalmin(m3h):
    return m3h * 0.004402867

def calcular_torre_resfriamento(tipo: str, vazao: int, temperatura: int):
    vazao_volumetrica_gal = m3h_para_kgalmin(vazao)
    if(tipo == "Torre de Resfriamento de Concreto"):

        if(temperatura == 10):
            f = 1
        elif(temperatura == 12):
            f = 1.5
        elif(temperatura == 15):
            f = 2

        pot = (vazao_volumetrica_gal ** 0.61)
        preco = (135 * f * pot) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Torre de Resfriamento de Madeira"):
        pot = (vazao_volumetrica_gal ** 0.85)
        preco = (33.9 * pot) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")