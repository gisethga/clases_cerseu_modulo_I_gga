"""
1. Crear 2 variables enteras, 2 variables flotantes, 2 variables string, 1 variable string que contiene
valor numérico y una variable boolean
2. Obtener y mostrar la suma de una variable entera con una variables string numérica
(Realizar conversión si fuera necesario)
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica
y la variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostrar el resultado de las parte entera, usando las varaibles enteras: //
6. Obtener una potencia usando una de las variables flotantes como base y
una variable entera como potencia

Nota: Las variables string pueden ser tu nombre y apellido
"""


print("____________________________________")
#Variables
print("____________________________________")
var_int1 = 5
var_int2 = 100
var_flt1 = 2.0
var_flt2 = 1.5
var_str1 = 5
var_str2 = 100
var_strnum1 = "123"
var_strbool1 = "true"
print("____________________________________")
print("Obtener y mostrar la suma de una variable entera con una variables string numérica")
print("variable entera: ",var_int1)
print("variable string: ",var_str1)
print(var_int1 + int(var_str1))
print("____________________________________")
print("Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica y la variable flotante")
print("variable entera: ",var_int1)
print("variable entera: ",var_int2)
print("variable string: ",var_str1)
print("variable flotante: ",var_flt1)
print(var_int1 + var_int2 + + int(var_str1)+ var_flt1)
print("____________________________________")
print("Obtener y mostrar el módulo de las variables enteras: %")
print("variable entera: ",var_int1)
print("variable entera: ",var_int2)
print(var_int1 % var_int2)
print("____________________________________")
print("Obtener y mostrar el resultado de las parte entera, usando las varaibles enteras: //")
print("variable entera: ",var_int1)
print("variable entera: ",var_int2)
print(var_int1 // var_int2)
print("____________________________________")
print("Obtener una potencia usando una de las variables flotantes como base y una variable entera como potencia")
print("variable flotante: ",var_flt1)
print("variable entera: ",var_int1)
print(var_flt1 ** var_int1)
print("____________________________________")

