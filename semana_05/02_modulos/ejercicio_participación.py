"""Intervención"""
"""Ejercicio módulos"""
"""
Requisitos:
    1. Crea un módulo donde se va a tener una función que obtiene el impuesto
    que va a pagar una persona si el sueldo es mayor a 500 soles, impuesto: 8%
    2. Ingresar el sueldo po consola, va a estar en un archivo principal
    Entregar solución al correo: docente.cerseu.unmsm@gmail.com
    
    Asunto: Participación  - Examen final

"""

def impuesto():
    sueldo = int(input("Ingrese el sueldo: "))
    if sueldo > 500:
        impt = sueldo * 0.08
    else:
        impt = 0
    return impt
