productos = ["Frijoles Refritos","Coca Cola","Zumo de Naranja", "Café de Olla", "Gorditas de Chicharrón", "Huevos Motuleños"]

productos_ordenados = sorted(productos)

cadena_ordenada = ", ".join(productos_ordenados)

crear_slug = lambda nombre: nombre.lower().replace(" ", "-")

slugs = list(map(crear_slug, productos))

print("Lista de slugs:",slugs)
print("Cadena de nombres en orden alfabético:", cadena_ordenada)