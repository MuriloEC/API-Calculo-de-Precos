import firebase_admin
from firebase_admin import credentials, firestore

# Esconder a chave antes de hospedar
cred = credentials.Certificate("C:/Users/muril/Downloads/calculadora-de-precos-adc8f-firebase-adminsdk-fbsvc-e325af59b1.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


'''pressure_dryer = {
    "Pressão Atmosférica": 1.0,
    "Vácuo": 2.0
}

for key, value in pressure_dryer.items():
    db.collection("Pressure_Dryer").document(key).set({"value": value})


material_dryer = {
    "Aço Macio": 1.0,
    "Inoxidável tipo 304": 1.4,
    "Forrado com Inoxidável 304-20%": 0.25,
    "Forrado com Inoxidável 316-20%": 0.50
}

for key, value in material_dryer.items():
    db.collection("Material_Dryer").document(key).set({"value": value})


material_spray_dryer = {
    "Aço Carbono": 0.33,
    "Aço Inoxidável 304": 1.0,
    "Aço Inoxidável 321": 1.0,
    "Aço Inoxidável 316": 1.13,
    "Monel": 3.0,
    "Inconel": 3.67
}

for key, value in material_spray_dryer.items():
    db.collection("Material_Spray_Dryer").document(key).set({"value": value})



drying_gas_dryer = {
    "Ar quente": 0.00,
    "Gás de Combustão (contato direto)": 0.12,
    "Gás de Combustão (contato indireto)": 0.35
}

for key, value in drying_gas_dryer.items():
    db.collection("DryingGas_Dryer").document(key).set({"value": value})

print("✅ Todas as tabelas foram inseridas no Firebase!")

tipo = [
    {"tipo": "Anéis Raschig de Cerâmica, 1 in.", "Cp": 19.6},
    {"tipo": "Anéis Raschig de Metal, 1 in.",   "Cp": 32.3},
    {"tipo": "Selas Intalox, 1 in.",       "Cp": 19.6},
    {"tipo": "Anéis Raschig de Cerâmica, 2 in.", "Cp": 13.6},
    {"tipo": "Anéis Raschig de Metal, 2 in.",   "Cp": 23},
    {"tipo": "Anéis Metálicos, 1 in.",      "Cp": 32.3},
    {"tipo": "Selas Intalox, 2 in.",       "Cp": 13.6},
    {"tipo": "Anéis Metálicos, 2 in.",      "Cp": 23},
]

# Inserindo os dados no Firebase
for tip in tipo:
    doc_ref = db.collection("tipo_empacotamento").document(tip["tipo"])
    doc_ref.set({
        "Cp": tip["Cp"]
    })



materiais = [
    {"material": "Aço Inoxidável, 304", "f1": 1.7},
    {"material": "Aço Inoxidável, 316", "f1": 2.1},
    {"material": "Carpenter 20CB-3",     "f1": 3.2},
    {"material": "Níquel - 200",           "f1": 5.4},
    {"material": "Monel - 400",            "f1": 3.6},
    {"material": "Inconel - 600",          "f1": 3.9},
    {"material": "Incoloy - 825",          "f1": 3.7},
    {"material": "Titânio",             "f1": 7.7},
]

# Inserindo os dados no Firebase
for mat in materiais:
    doc_ref = db.collection("materiais_destilador").document(mat["material"])
    doc_ref.set({
        "f1": mat["f1"]
    })

print("Dados enviados com sucesso para o Firebase!")


tray_types = [
    {"type": "Válvula", "f3": 1.00},
    {"type": "Grade", "f3": 0.80},
    {"type": "Tampa de Bolha", "f3": 1.59},
    {"type": "Peneira (com tubo descendente)", "f3": 0.85},
]

# Inserindo no Firebase
for tray in tray_types:
    doc_ref = db.collection("tray_types_destilador").document(tray["type"])
    doc_ref.set({
        "f3": tray["f3"]
    })

print("Tabela Tray Types enviada para o Firebase com sucesso!")



coeficientes_fans = {
    "Lâmina Radial": {"a": 0.4692, "b": 0.1203, "c": 0.0931},
    "Lâmina Curvada para Trás": {"a": 0.0400, "b": 0.1821, "c": 0.0786},
    "Hélice": {"a": -0.4456, "b": 0.2211, "c": 0.0820},
    "Hélice com Palhetas Guia": {"a": -1.0181, "b": 0.3332, "c": 0.0647}
}

# Inserção no Firestore
for tipo, valores in coeficientes_fans.items():
    doc_ref = db.collection("coeficientes_fans").document(tipo)
    doc_ref.set(valores)
    print(f"Inserido: {tipo} -> {valores}")

print("✅ População concluída com sucesso.")


fatores_materiais = {
    "Aço Carbono": 2.2,
    "Fibra de Vidro": 4.0,
    "Aço Inoxidável": 5.5,
    "Liga de Níquel": 11.0
}

# Inserção no Firestore
for material, fator in fatores_materiais.items():
    doc_ref = db.collection("fatores_materiais").document(material)
    doc_ref.set({"fator_m": fator})
    print(f"Inserido: {material} -> fator_m: {fator}")

print("✅ Fatores de materiais populados com sucesso.")'''


# Fatores de pressão
'''fatores_pressao = {
    1: {"Radial": 1.00, "Backward Curved": 1.00, "Propeller": 1.00, "Vane": 1.00},
    2: {"Radial": 1.15, "Backward Curved": 1.15, "Propeller": None, "Vane": 1.15},
    4: {"Radial": 1.30, "Backward Curved": 1.30, "Propeller": None, "Vane": 1.30},
    6: {"Radial": 1.45, "Backward Curved": 1.45, "Propeller": None, "Vane": None},
    16: {"Radial": 1.60, "Backward Curved": None, "Propeller": None, "Vane": None}
}

# Inserção no Firestore
for pressao, tipos in fatores_pressao.items():
    doc_ref = db.collection("fatores_pressao").document(f"{pressao}kPa")
    doc_ref.set(tipos)
    print(f"Inserido: {pressao}kPa -> {tipos}")

print("✅ Fatores de pressão populados com sucesso.")'''







'''coeficientes = {
    "Impelidor Único": {
        "Aço Carbono": {
            "Baixa": {"a": 8.57, "b": 0.1195, "c": 0.0819},
            "Média": {"a": 8.43, "b": -0.0880, "c": 0.1123},
            "Alta": {"a": 8.31, "b": -0.1368, "c": 0.1015},
        },
        "Aço 316": {
            "Baixa": {"a": 6.62, "b": 0.2474, "c": 0.0654},
            "Média": {"a": 8.55, "b": 0.0308, "c": 0.0643},
            "Alta": {"a": 6.52, "b": -0.1802, "c": 0.1158},
        }
    },
    "Impelidor Duplo": {
        "Aço Carbono": {
            "Baixa": {"a": 8.80, "b": 0.1603, "c": 0.0659},
            "Média": {"a": 8.50, "b": 0.0257, "c": 0.0878},
            "Alta": {"a": 6.43, "b": -0.1981, "c": 0.1239},
        },
        "Aço 316": {
            "Baixa": {"a": 9.25, "b": 0.2801, "c": 0.0542},
            "Média": {"a": 8.82, "b": 0.1235, "c": 0.0818},
            "Alta": {"a": 6.72, "b": -0.1225, "c": 0.1075},
        }
    }
}

# Inserir no Firestore
for tipo, materiais in coeficientes.items():
    for material, faixas in materiais.items():
        for faixa, valores in faixas.items():
            doc_ref = db.collection("coeficientes").document(tipo).collection(material).document(faixa)
            doc_ref.set(valores)
            print(f"Inserido: {tipo} > {material} > {faixa} -> {valores}")

print("✅ População concluída com sucesso.")'''