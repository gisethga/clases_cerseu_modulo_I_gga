
def dividir(valor_1, valor_2):
    try:
        result = valor_1 / valor_2
    except ZeroDivisionError:
        print("El numero no puede dividir")
        raise ValueError(f"El numero no puede dividir: {valor_1} y {valor_2}")
    else:
        return result


try:
    dividir(18, 0)
except ValueError as error:
    print("Error captura afuera : {}".format(error))










