""""LISTAS PYTHON"""
"""
Lista: Caso de actualización de notas
"""

notas =[12, 18, 16, 20, 11, 14, 13]

i=0

for nota in notas:
    print(notas[i])
    notas[i] = nota - 2
    print("Nota actualizada: {}".format(notas[i]))
    i += 1

print(notas)

#La nueva lista actualizada tendrá la mitad del valor de cada nota
#Agregar dos notas en la lista que sean mayores a la las notas de la lista actualizada

id= 0
for nota in notas:
    notas[id] = nota/2
print(notas)
notas.append(19)
notas.append(20)
print(notas)


