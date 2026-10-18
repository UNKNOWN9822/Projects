from calculos import aplicar_descuento

def test_calcular_descuento_tornillos_():
    resultado = aplicar_descuento(1500, 50)
    assert resultado == 750