from calculos import aplicar_descuento

def test_calcular_descuento_cincuenta_():
    resultado = aplicar_descuento(2000, 50)
    assert resultado == 1000

def test_calcular_descuento_menosDos_():
    resultado = aplicar_descuento(1500, -2)
    assert resultado == 1530

def test_calcular_descuento_cientoUno():
    resultado = aplicar_descuento(3000, 101)
    assert resultado == -30