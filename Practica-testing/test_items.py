from calculos import calcular_subtotal


items = [{"precio": 1500, "cantidad": 2}, {"precio": 800, "cantidad": 3}, {"precio": 1, "cantidad": 2}, ]

resultado = calcular_subtotal(items)
assert resultado == 5402
