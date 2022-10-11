producto = input("Introduzca el nombre del producto:\n")
precio = float(input("Introduzca el precio:\n"))
unidad = float(input("Introduzca la cantidad:\n"))
total = (precio * unidad)
print("Tu producto es", producto, ", el precio unitario es de{precio:6.2f}€, el total de unidad es de{unidad:3.0f}, el total seria de{total:8.2f}€"
     .format(producto = producto, precio = precio, unidad = unidad, total = total))