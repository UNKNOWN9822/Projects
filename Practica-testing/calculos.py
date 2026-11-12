def calcular_total(precio_unitario, cantidad):
    return precio_unitario * cantidad
    
def aplicar_descuento(monto, porcentaje):
    return monto - (monto * porcentaje / 100)

def calcular_total_presupuesto(items, porcentaje_descuento):
    subtotal = 0
    for item in items:
        subtotal += item["precio"] * item["cantidad"]  
    total = subtotal - (subtotal * porcentaje_descuento / 100) 
    return total

def calcular_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item["precio"] * item["cantidad"]
    return subtotal

def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    if zona == "centrica":
        zona = 8000
    elif zona == "periferica":
        zona = 12000
    elif zona == "exterior":
        zona = 18000
    if trabajo_mismo_dia == True:
        zona = zona * 0
    if es_fin_de_semana == True:
        zona = zona * 1.50

    return zona
class HorarioInvalidoError(ValueError):
		pass
def validar_turno(fecha, hora):
    if hora <= "18:00" and hora >= "10:00": 
        return "todo correcto y agendado"
    else: 
        raise HorarioInvalidoError("Horario fuera del rango permitido")
