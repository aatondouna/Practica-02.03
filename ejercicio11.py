producto = input("Introduzca el nombre del producto:\n")
precio = float(input("Introduzca el precio:\n"))
unidad = float(input("Introduzca la cantidad:\n"))
total = precio * unidad
print("Tu compra es", producto, "el valor es de{precio:6.2f}€:\n "
                                "el total de unidad es de:{unidad:3.0f}\n el total seria de:{total:8.2f}€"
      .format(producto=producto, precio=precio, unidad=unidad, total=total))
