from calculos import calcular_visita
"""
El plomero cobra una visita a domicilio según la zona:
● Zona céntrica: $8.000
● Zona periférica: $12.000
● Fuera de la ciudad: $18.000
Además:
● Si el trabajo se hace el mismo día de la visita, no se cobra la visita.
● Los sábados, domingos y feriados se recarga un 50% sobre el valor de la visita.
"""

visita = {"zona": "arriba", "trabajo_mismo_dia": False, "es_fin_de_semana": False}

resultado = calcular_visita(visita)
assert resultado == 18000