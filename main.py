from fastapi import FastAPI, Query
from services.calcular_agitador import calcular_agitador
from services.calcular_torre_resfriamento import calcular_torre_resfriamento
from services.calcular_transportador import calcular_transportadora
from services.calcular_britador import calcular_britador
from services.calcular_compressor_turbinas_fans import calcular_compressor, calcular_turbina
from services.calcular_destilador import calcular_destilador_packed, calcular_destilador_tray, calcular_torre_absorcao_packed, calcular_torre_absorcao_tray
from services.calcular_secador import calcular_secador_rotary_combustion_gas_heated, calcular_secador_hot_air_heated, calcular_secador_rotary_steam_tube, calcular_secador_cabinet_dryer, calcular_secador_spray_dryer, calcular_secador_multiple_hearth_furnaces
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # URL do Angular em desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.get("/api/calcular/agitador")
def calcular(tipo: str = Query(...), material: str = Query(...), velocidade: float = Query(...), hp: int = Query(...)):
    resultado = calcular_agitador(tipo, material, velocidade, hp)
    return {"resultado": resultado}

@app.get("/api/calcular/britador")
def calcular(vazao: int = Query(...), tipo: str = Query(...)):
    resultado = calcular_britador(vazao, tipo)
    return {"resultado": resultado}

@app.get("/api/calcular/compressor")
def calcular(hp: int = Query(...), tipo: str = Query(...)):
    resultado = calcular_compressor(hp, tipo)
    return {"resultado": resultado}

@app.get("/api/calcular/turbina")
def calcular(hp: int = Query(...), tipo: str = Query(...)):
    resultado = calcular_turbina(hp, tipo)
    return {"resultado": resultado}

'''@app.get("/api/calcular/ventilador")
def calcular(tipo: str = Query(...), material: str = Query(...), pressao: int = Query(...), vazao: float = Query(...)):
    resultado = calcular_ventilador(tipo, material, pressao, vazao)
    return {"resultado": resultado}'''

@app.get("/api/calcular/transportador")
def calcular(comprimento: int = Query(...), tipo: str = Query(...), vazao: int = Query(...)):
    resultado = calcular_transportadora(comprimento, tipo, vazao)
    return {"resultado": resultado}

@app.get("/api/calcular/destilador_bandeja")
def calcular(material: str = Query(...), tipo_bandeja: str = Query(...), N:float = Query(...), W:float = Query(...), Tb:float = Query(...), Tp:float = Query(...), L:float = Query(...), D:float = Query(...)):
    resultado = calcular_destilador_tray(material, tipo_bandeja, N, W, Tb, Tp, L, D)
    return {"resultado": resultado}

@app.get("/api/calcular/torre_absorcao_bandeja")
def calcular(material: str = Query(...), tipo_bandeja: str = Query(...), N:float = Query(...), W:float = Query(...), L:float = Query(...), D:float = Query(...)):
    resultado = calcular_torre_absorcao_tray(material, tipo_bandeja, N, W, L, D)
    return {"resultado": resultado}

@app.get("/api/calcular/destilador_embalado")
def calcular(material: str = Query(...), W:float = Query(...), Tb:float = Query(...), Tp:float = Query(...), L:float = Query(...), D:float = Query(...), V:float = Query(...), tipo: str = Query(...)):
    resultado = calcular_destilador_packed(material, W, Tb, Tp, L, D, V, tipo)
    return {"resultado": resultado}

@app.get("/api/calcular/torre_absorcao_embalada")
def calcular(material: str = Query(...), W:float = Query(...), L:float = Query(...), D:float = Query(...),  V:float = Query(...), tipo: str = Query(...)):
    resultado = calcular_torre_absorcao_packed(material, W, L, D, V, tipo)
    return {"resultado": resultado}

@app.get("/api/calcular/secador_combustao")
def calcular(material: str = Query(...), tipo_gas: str = Query(...), area: float = Query(...)):
    resultado = calcular_secador_rotary_combustion_gas_heated(material, tipo_gas, area)
    return {"resultado": resultado}

@app.get("/api/calcular/secador_ar_quente")
def calcular(material: str = Query(...), tipo_gas: str = Query(...), area: float = Query(...)):
    resultado = calcular_secador_hot_air_heated(material, tipo_gas, area)
    return {"resultado": resultado}

@app.get("/api/calcular/secador_tubo_vapor")
def calcular(material: str = Query(...), area: float = Query(...)):
    resultado = calcular_secador_rotary_steam_tube(material, area)
    return {"resultado": resultado}

@app.get("/api/calcular/secador_gabinete")
def calcular(tipo_pressao: str = Query(...), area: float = Query(...)):
    resultado = calcular_secador_cabinet_dryer(tipo_pressao, area)
    return {"resultado": resultado}

@app.get("/api/calcular/secador_spray")
def calcular(material: str = Query(...), vazao: float = Query(...)):
    resultado = calcular_secador_spray_dryer(material, vazao)
    return {"resultado": resultado}

@app.get("/api/calcular/secador_forno")
def calcular(n_lareira: int = Query(...), diametro: str = Query(...)):
    resultado = calcular_secador_multiple_hearth_furnaces(n_lareira, diametro)
    return {"resultado": resultado}

@app.get("/api/calcular/torrederesfriamento")
def calcular(tipo: str = Query(...),vazao: int = Query(...), temperatura: int = Query(...)):
    resultado = calcular_torre_resfriamento(tipo, vazao, temperatura)
    return {"resultado": resultado}