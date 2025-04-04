from functools import reduce

tipo_cambio = 20.40

ventas_mxn = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

prom_mxn = reduce(lambda x, y: x + y, ventas_mxn) / len(ventas_mxn)

ventas_usd = list(map(lambda mxn: mxn / tipo_cambio, ventas_mxn))

ventas_may_150 = list(filter(lambda usd: usd > 150, ventas_usd))

suma_mayores_150 = reduce(lambda x, y: x + y, ventas_may_150, 0)

print("El promedio de ventas en pesos mexicanos:", prom_mxn)
print("Las ventas de la semana en dolares:",ventas_usd)
print("Las ventas en dólares mayores a 150:",ventas_may_150)
print("La suma total de las ventas en dólares mayores a 150.:",suma_mayores_150)

