"""
Ejercicio 03 - Decoradores
Requisitos:

* Crear un decorador llamado validar_positivos que verifique que todos los argumentos numéricos de una función
sean mayores que 0.
* Si algún argumento no cumple la condición, debe lanzar un ValueError con el mensaje
"Todos los argumentos deberán ser positivos".
* Aplicar el decorador sobre una función calcular_promedio(*args) que
reciba una cantidad variable de números y retorne el promedio. Y mostrar también la cantidad de parámetros de
la función

Probar la función con 3 casos correctos y uno que lance la excepción

"""