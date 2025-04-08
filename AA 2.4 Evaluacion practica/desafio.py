"""
Objetivo: Programa para que los alumnos realicen la encuesta de evaluación de 
sus asignaturas, donde puedan calificar aspectos de las materias de su carrera y 
analizar los resultados mediante funciones de orden superior en Python.
"""

from functools import reduce

respuestas = []

def promedio_aspecto(aspecto, datos):
  
    valores = list(map(lambda d: d[aspecto], datos))
    total = reduce(lambda a, b: a + b, valores, 0)
    return total / len(valores) if valores else 0

def filtrar_por_aspecto(aspecto, minimo, datos):

    return list(filter(lambda d: d[aspecto] >= minimo, datos))

def suma_recursiva(lista):
   
    if not lista:
        return 0
    return lista[0] + suma_recursiva(lista[1:])

def ingresar_respuesta():
    
    materia = input("Nombre de la materia: ")
    actividades = int(input("Calificación de actividades (1-5): "))
    herramientas = int(input("Calificación de herramientas (1-5): "))
    contenido = int(input("Calificación de contenido (1-5): "))
    respuestas.append({
        "materia": materia,
        "actividades": actividades,
        "herramientas": herramientas,
        "contenido": contenido
    })

def mostrar_resultados():
    
    if not respuestas:
        print("No hay respuestas registradas.")
        return
    print("\n--- Resultados de la Encuesta ---")
    for aspecto in ["actividades", "herramientas", "contenido"]:
        promedio = promedio_aspecto(aspecto, respuestas)
        print(f"Promedio de {aspecto}: {promedio:.2f}")

    buenas_materias = [d["materia"] for d in respuestas if d["actividades"] >= 4]
    print("Materias con buenas actividades:", ", ".join(buenas_materias))

def menu():
    while True:
        print("\n1. Ingresar evaluación")
        print("2. Ver resultados")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ingresar_respuesta()
        elif opcion == "2":
            mostrar_resultados()
        elif opcion == "3":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()