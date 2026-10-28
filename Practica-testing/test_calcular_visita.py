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

def test_calcular_visita_caso1():
    resultado = calcular_visita("centrica", False, False)
    assert resultado == 8000

def test_calcular_visita_caso2():
    resultado = calcular_visita("periferica", False, False)
    assert resultado == 12000

def test_calcular_visita_caso3():
    resultado = calcular_visita("exterior", False, False)
    assert resultado == 18000

def test_calcular_visita_caso4():
    resultado = calcular_visita("periferica", True, False)
    assert resultado == 0

def test_calcular_visita_caso5():
    resultado = calcular_visita("centrica", False, True)
    assert resultado == 12000

def test_calcular_visita_caso6():
    resultado = calcular_visita("periferica", True, True)
    assert resultado == 0

def test_calcular_visita_caso7():
    resultado = calcular_visita("superior", False, True)
    assert resultado == 18000