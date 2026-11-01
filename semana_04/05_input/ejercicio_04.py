
"""Intervención"""
"""
Requisitos:
- Dentro de una empresa se va solicitar pedir el nombre y apellido del empleado (input)
- Distrito de residencia ingresado por teclado
- Sueldo y cálculo del bono final de año: que será el triple del sueldo mensual menos el 10% del sueldo
- Todos estos datos se van a ingresar a un diccionario
- Asignar a 3 variables los valores del diccionario
- Mostrar por la terminal (output) el mensaje de: "'Nombre' 'Apellido', recibirá 'bono' soles de fin de año"
"""

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
distrito = input("Ingrese el distrito: ")
sueldo = float(input("Ingrese el sueldo: "))

bono = sueldo * 3 - (0.10 * sueldo)

diccionario = {"Nombre": nombre,
                "Apellidos" : apellido,
                "Distrito": distrito,
                "Sueldos" : sueldo,
                "bono": bono}

print("su nombre es: {} ,su apellido es {} y recibira un bono de {} soles de fin de año".format(nombre, apellido, bono))










