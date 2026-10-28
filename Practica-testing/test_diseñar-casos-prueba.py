from calculos import calcular_total_presupuesto

def test_calcular_precio_normal():
    items = [{"precio": 1000, "cantidad": 0}]
    resultado = calcular_total_presupuesto(items, 70)
    assert resultado == 0

def test_calcular_total_presupuesto_cincuenta_():
    items = [{"precio": 0.1, "cantidad": 1}]
    resultado = calcular_total_presupuesto(items, 50)
    assert resultado == 0.05

def test_calcular_cantidad_normal():
    items = [{"precio": 100, "cantidad": 5}]
    resultado = calcular_total_presupuesto(items, 50)
    assert resultado == 250

def test_calcular_menor_precio_positivo_centavos():
    items = [{"precio": 0.1, "cantidad": 1}]
    resultado = calcular_total_presupuesto(items, 50)
    assert resultado == 0.05

def test_descuento_mas_grande():
    items = [{"precio": 100, "cantidad": 3}]
    resultado = calcular_total_presupuesto(items, 100)
    assert resultado == 0

def test_descuento_cero():
    items = [{"precio": 100, "cantidad": 1}]
    resultado = calcular_total_presupuesto(items, 0)
    assert resultado == 100

def test_items_cero():
    items = [{"precio": 0, "cantidad": 0}]
    resultado = calcular_total_presupuesto(items, 100)
    assert resultado == 0

def test_error_string_porcentaje_descuento():
    items = [{"precio": 100, "cantidad": 1}]
    resultado = calcular_total_presupuesto(items, "hola")
    assert resultado == 100

def test_error_string_precio_cantidad():
    items = [{"precio": hola, "cantidad": adios}]
    resultado = calcular_total_presupuesto(items, 100)
    assert resultado == 100

def test_error_sin_dato_items():
    items = [{"precio": None, "cantidad": None}]
    resultado = calcular_total_presupuesto(items, 0)
    assert resultado == 100