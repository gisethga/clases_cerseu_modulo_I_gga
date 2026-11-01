

# Diccionario de inventario
ventas = {
    "Laptop": 3500,
    "Mouse": 250,
    "Teclado": 540,
    "Monitor": 1200,
    "Impresora": 850
}

contador = 0
#Agregamos un nuevo producto
ventas["Webcam"] = 29
#Modificamos la cantidad de Mouse
ventas["Mouse"] = 300
#variables para el analisis
total_venta = 0
mayor_venta = 0
producto_mayor_venta = 0
conatdor = 0
for producto in ventas:
    monto = ventas[producto]
    print("{}: S/.{}". format(producto, monto))

    #sumar ventas
    total_venta += monto

    #obtener el producto con mayor venta
    if monto > mayor_venta:
        mayor_venta = monto
        producto_mayor_venta = producto

    if monto > 500:
        contador += 1


print("Total de ventas: {}". format(total_venta))
print("Mayor venta: {}".format(mayor_venta))
print("Producto mayor venta: {}".format(producto_mayor_venta))
print("Importe mayor:", total_venta)




