"""Intervención"""

"""
Requisitos:
- Crear una lista de notas, 10 notas
- Obtener la suma de notas, utilizando el recorrido, apoyarse de una variable auxiliar
- Obtener las notas aprobadas y desaprobadas, empezar con listas vacías
- Obtener el promedio de notas, dentro de una variable
- Mostrar la nota más baja y la más alta

"""

notas =[16, 18, 17, 12, 11, 14, 13, 15, 14, 19]
print("La lista de nostas es:", notas)
suma_nota = 0
aprobado = []
desaprobado = []
for nota in notas:
    suma_nota += nota

    if nota > 13:
        aprobado.append(nota)
    else:
        desaprobado.append(nota)

print("La suma de notas es: {}".format(suma_nota))
print("Notas aprobadas:", aprobado)
print("Notas desaprobadas:", desaprobado)
promedio = suma_nota / len(notas)
print("El promedio de notas:", promedio)

i=0
for alta in aprobado:
    i > alta
    i = alta

e=20
for baja in desaprobado:
    e < baja
    e = baja

print("Notas mas alta:", i)
print("Notas mas baja:", e)



