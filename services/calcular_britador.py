from services.calcular_agitador import get_dolar_bcb

def calcular_britador(vazao: int, tipo: str) -> float:

    if(tipo == "Britador Cônico"):
        vazao_ton = (vazao/1000)
        vazao_w = (vazao_ton ** 1.05)
        preco = (vazao_w * 1.55) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Britador Giratório"):
        vazao_ton = (vazao/1000)
        vazao_w = (vazao_ton ** 0.6)
        preco = (vazao_w * 8) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Britador de Mandíbula"):
        vazao_ton = (vazao/1000)
        vazao_w = (vazao_ton ** 0.57)
        preco = (vazao_w * 6.3) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Moinho de Martelo"):
        vazao_ton = (vazao/1000)
        vazao_w = (vazao_ton ** 0.78)
        preco = (vazao_w * 2.44) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Moinho de Bolas"):
        vazao_ton = (vazao/1000)
        vazao_w = (vazao_ton ** 0.69)
        preco = (vazao_w * 50) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")
    
    elif(tipo == "Pulverizador"):
        vazao_ton = (vazao/1000)
        vazao_w = (vazao_ton ** 0.39)
        preco = (vazao_w * 22.6) * 1000
        preco_reais = preco * get_dolar_bcb()
        return "{:.2f}".format(preco_reais).replace(".", ",")