def calcular_total(precio_unitario, cantidad):
    return precio_unitario * cantidad
    
def aplicar_descuento(monto, porcentaje):
    return monto - (monto * porcentaje / 100)

def calcular_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item["precio"] * item["cantidad"]
    return subtotal

def calcular_visita(visita):
    if visita["zona"] == "central":
        visita["zona"] = 8000
    if visita["trabajo_mismo_dia"] == True:
        visita["zona"] = 0
    if visita["es_fin_de_semana"] == True:
        visita["zona"] = visita["zona"] * 1.5
    return visita["zona"]

    