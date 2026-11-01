"""
Ejercicio 08
Participación"""

""" 
Ejercicio Participación: Manejo de excepciones en listas

**Objetivo:** 
Aplicar el manejo de excepciones en Python para controlar errores al intentar modificar elementos de una lista.

**Requisitos:**

1. Crear una función que reciba dos parámetros: una lista y un índice.
2. Definir una lista que contenga inicialmente **4 elementos numéricos**.
3. Dentro de la función, intentar modificar el elemento correspondiente al índice recibido, asignándole el valor de `0`.
4. Si el índice no existe en la lista, controlar la excepción y agregar un nuevo elemento con el valor de `0` al final de la lista.
5. Mostrar la lista original y la lista final después de ejecutar la función.
6. Realizar dos pruebas:
   - **Caso 1:** Utilizar un índice existente.
   - **Caso 2:** Utilizar un índice que esté fuera del rango de la lista.

**Indicaciones de entrega:**

- Correo: docente.cerseu.unmsm@gmail.com
- Asunto: Participación para práctica 02
- Fecha límite: Domingo 01, hasta las 10:00 p. m.
- Archivos: Enviar en un mismo correo los ejercicios de participación

"""
def func (lista, indice):
    print("La lista original es: {}".format(lista))
    try:
        lista[indice] = 0
        print("La nueva lista es: {}".format(lista))
    except IndexError:
        lista.append(0)
        print("Error de índice: {}, está fuera del rango de la lista, su rango es de: 0 a {} ".format(indice, len(lista)-1))
        print("La nueva lista es: {}".format(lista))

lista = []
lista = input("Introduce una lista de 4 elementos númericos:")
lista = lista.split(",")
indice = int(input("Introduce un indice:"))
func (lista, indice)

































