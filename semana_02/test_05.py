"""
Requisitos:

1. Crear dos variables para los valores de nombre, profesion y ciudad
2. Crear dos varaibles para la remuneración de enero y febrero (mayor a 1500)
3. Crear 1 varibles donde se sumará el ingreso de los dos meses: enero y febrero
4. Mostrar en pantalla el siguiente mensaje (Output)

"Hola soy 'nombre', soy 'profesión' y mi remuneración acumulada es de ''remunera_total"

rem_1
remunera_1
rem_enero

"""

nombre = "Juan"
profesion = "Profesor"
ciudad = "Lima"
rem_Ene = 1700
rem_Feb = 1750
rem_total = rem_Ene + rem_Feb

print("Hola soy {} , soy {} y mi remuneración acumulada es de {} ".format(nombre, profesion, rem_total))
