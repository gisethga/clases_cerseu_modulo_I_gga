"""
excepción personalizada
"""

def validar_edad(edad):
    if edad < 0:
    raise ValueError("El valor de edad debe ser mayor que 0")
    print("Edad correcta")
    return True


validar_edad(18)
validar_edad(-5)






