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

def validar_positivos(funcion):
    def validar(*args):
        print("Los argumentos recibidos son: ", args)
        print(f"La cantida de argumentos recibidos es: {len(args)}")
        for num in args:
            if num <= 0:
                raise ValueError("Los argumentos deben ser mayores a cero")

        return funcion(*args)
    return validar

@validar_positivos
def calcular_promedio(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print("\n CASO 1")
res1 = calcular_promedio(12.5, 18, 14, 16.5)
print(f"Resultado Promedio: {res1:.2f}")

print("\n CASO 2")
res2 = calcular_promedio(15, 15)
print(f"Resultado Promedio: {res2:.2f}")

print("\n CASO 3")
res3 = calcular_promedio(10, 20, 30)
print(f"Resultado Promedio: {res3:.2f}")


print("\n CASO 4")
try:
    res4 = calcular_promedio(10, -5, 20)
    print(f"Resultado Promedio: {res4:.2f}")
except ValueError as e:
    print(f"Se produjo una excepción -> ValueError: {e}")