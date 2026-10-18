from calculos import aplicar_descuento

def test_calcular_descuento_pan_viejo_():
    resultado = aplicar_descuento(3000, 0)
    assert resultado == 3000