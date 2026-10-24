productos = []
cantidades = []


def leer_cantidad(mensaje):
    texto = input(mensaje).strip()
    while not texto.isdigit():
        print("Cantidad no valida. Ingrese un numero entero mayor a 0.")
        texto = input(mensaje).strip()
    return int(texto)


def buscar_indice(nombre):
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            return i
    return -1


def registrar_producto():
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacio, vuelva a intertarlo.")
    elif buscar_indice(nombre) != -1:
        print("El producto ya esta registrado. Use la opcion 4 para modificar su cantidad.")
    else:
        cantidad = leer_cantidad("Cantidad disponible: ")
        productos.append(nombre)
        cantidades.append(cantidad)
        print("Producto registrado.")


def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario esta vacio, vuelva a intertarlo cuando se registren productos.")
    else:
        print("\n--- INVENTARIO ---")
        for i in range(len(productos)):
            print(i + 1, productos[i], "- cantidad:", cantidades[i])


def buscar_producto():
    nombre = input("Nombre del producto a buscar: ").strip()
    indice = buscar_indice(nombre)
    if indice == -1:
        print("El producto no existe en el inventario, vuelva a intentarlo. ")
    else:
        print("Producto encontrado:", productos[indice], "- cantidad:", cantidades[indice])


def modificar_cantidad():
    nombre = input("Nombre del producto a modificar: ").strip()
    indice = buscar_indice(nombre)
    if indice == -1:
        print("El producto no existe en el inventario, vuelva a intentarlo. ")
    else:
        print("Cantidad actual de", productos[indice], ":", cantidades[indice])
        cantidades[indice] = leer_cantidad("Nueva cantidad del producto: ")
        print("Cantidad del producto actualizada.")


def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ").strip()
    indice = buscar_indice(nombre)
    if indice == -1:
        print("El producto no existe en el inventario, vuelve a intentarlo. ")
    else:
        eliminado = productos.pop(indice)
        cantidades.pop(indice)
        print("Producto eliminado:", eliminado)


def mostrar_resumen():
    print("Productos registrados:", len(productos))


def mostrar_mayor_cantidad():
    if len(productos) == 0:
        print("El inventario esta vacio, vuelva a intentarlo. ")
    else:
        indice_mayor = 0
        for i in range(len(cantidades)):
            if cantidades[i] > cantidades[indice_mayor]:
                indice_mayor = i
        print("Producto con mayor cantidad:", productos[indice_mayor],
              "- cantidad:", cantidades[indice_mayor])


def mostrar_menu():
    print("\n===== GESTOR DE INVENTARIO =====")
    print("1. Registrar un producto")
    print("2. Mostrar resumen de inventario")
    print("3. Buscar producto")
    print("4. Modificar cantidad de producto")
    print("5. Eliminar producto")
    print("6. Mostrar cuantos productos diferentes hay")
    print("7. Mostrar producto con mayor cantidad")
    print("8. Salir")


def main():
    opcion = ""
    while opcion != "8":
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            mostrar_resumen()
        elif opcion == "7":
            mostrar_mayor_cantidad()
        elif opcion == "8":
            print("Saliendo del programa. ¡Hasta pronto!")
        else:
            print("Opcion no valida. Vuelva a escojer una de las opciones dadas.")


main()
