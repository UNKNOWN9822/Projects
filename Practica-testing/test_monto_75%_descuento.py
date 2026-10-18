from calculos import aplicar_descuento

def test_calcular_descuento_pan_viejo_():
    resultado = aplicar_descuento(2000, 75)
    assert resultado == 500