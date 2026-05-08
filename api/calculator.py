from fastapi import FastAPI
from services.calculator import calcular_valor

app=FastAPI()

@app.get("/api/calcular")
def calcular(a: float, b: float, c:float, HP: int):
    resultado = calcular_valor(a, b, c, HP)
    return {"resultado": resultado}
