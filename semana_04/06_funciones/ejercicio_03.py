"""
Participación
"""

"""
Ejercicio 03
Participación

Requisitos:
- Crear una función que multiplicará 4 valores (int y floats)
- La función tendrá un parámetro que contendrá un valor por defecto
- Mostrar 2 casos donde se ingresó los valores donde uno no afectará el valor del parámetro
que ya contiene un valor y otro donde si lo estará afectando
- Ingresar los valores por consola

"""

def multiplicar( valor1, valor2, valor3,valor4 = 10):
    return valor1 * valor2 * valor3 * valor4

valor_1= int(input("Introduce un número entero: "))
valor_2= float (input("Introduce un número decimal: "))
valor_3= int(input("Introduce otro número entero: "))

caso_1 = multiplicar(valor_1, valor_2, valor_3)
print("El valor de la multiplicación es: {}".format(caso_1))
caso_2 = multiplicar(valor_1, valor_2, valor_3,20)
print("El valor de la multiplicacion es: {}".format(caso_2))
























