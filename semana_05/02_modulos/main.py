#import funciones
from funciones import suma as opera_1, multiplica as opera_2, eleva as opera_3


var_1 = int(input("Ingresa primer número: "))
var_2 = int(input("Ingresa segundo número: "))


#sum = funciones.suma(var_1, var_2)
sum = opera_1(var_1, var_2)
print(sum)

#mul = funciones.multiplica(var_1, var_2)
mul = opera_2(var_1, var_2)
print(mul)

elev = opera_3(var_1, var_2)
print(elev)

from ejercicio_participación import impuesto as opera_4
resultado = opera_4()
if resultado > 0:
    print(f"El sueldo es mayor a 500 por lo que el impuesto es {resultado:.2f}")
else:
    print("El sueldo es menor a 500 por lo que no se aplica el impuesto")
