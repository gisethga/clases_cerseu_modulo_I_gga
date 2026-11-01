"""Intervención"""
from django.db.models.functions import Upper

"""
Usando propiedades de string
Requisitos:
    - Ingresar su nombre y apellido por consola (variables distintas)
    - Obtener el tamaño de tu nombre completo y muéstralo en consola
    - Imprimir el resultado final, todo en mayúsculas: .upper()
    - Indicar mediante condicionales si el tamaño del nombre es mayor o no al apellido ingresado
    - Solamente ingresar el apellido paterno

"""

nombre = input("Nombre: ")
apellido = input("Apelido: ")
print("El tamaño de mi nombre es:", format(len(nombre)))
nombre_completo = nombre + " " + apellido
print(nombre_completo.upper())

if len(nombre) > len(apellido):
    print("Apellido paterno tiene menor longitud")
elif len(nombre) < len(apellido):
    print("Apellido paterno tiene mayor longitud")
else len(nombre) = len(apellido):
    print("El nombre y Apellido, tienen la misma longitud")














