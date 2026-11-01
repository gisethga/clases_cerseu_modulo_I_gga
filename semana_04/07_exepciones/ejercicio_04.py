"""Manejo de errores"""
"""
    Crear un programa usando exepciones donde no se puede
    realizar la suma entre diferentes tipos de datos
"""

def operaciones(a, b):
    try:
        resultado_1 = a + b
        resultado_2 = a / b
    except TypeError:
        print("No se puede realizar una operación de un 'string' con un dato entero")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    else:
        print("Resultado: ", resultado_1)
        print("Resultado: ", resultado_2)

operaciones(40, "Arequipa")
operaciones(40, 0)
operaciones(40, 10)
operaciones("viaje a ", "Arequipa")