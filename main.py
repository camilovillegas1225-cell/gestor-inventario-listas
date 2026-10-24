# Gestor de inventario con listas paralelas
# El elemento en el indice i de "productos" y de "cantidades"
# corresponde al mismo producto.

productos = []
cantidades = []


def leer_cantidad(mensaje):
    # Pide un numero entero no negativo hasta que sea valido
    texto = input(mensaje).strip()
    while not texto.isdigit():
        print("Cantidad no valida. Ingrese un numero entero mayor o igual a 0.")
        texto = input(mensaje).strip()
    return int(texto)


def buscar_indice(nombre):
    # Devuelve el indice del producto o -1 si no existe.
    # Se compara sin distinguir mayusculas/minusculas.
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            return i
    return -1


def registrar_producto():
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacio.")
    elif buscar_indice(nombre) != -1:
        # Decision: no se permite registrar dos veces el mismo producto,
        # para que cada nombre tenga una sola cantidad y las listas
        # paralelas se mantengan consistentes.
        print("El producto ya esta registrado. Use la opcion 4 para modificar su cantidad.")
    else:
        cantidad = leer_cantidad("Cantidad disponible: ")
        productos.append(nombre)
        cantidades.append(cantidad)
        print("Producto registrado.")


def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        print("\n--- INVENTARIO ---")
        for i in range(len(productos)):
            print(i + 1, productos[i], "-", cantidades[i])


def buscar_producto():
    nombre = input("Nombre del producto a buscar: ").strip()
    indice = buscar_indice(nombre)
    if indice == -1:
        print("El producto no existe en el inventario.")
    else:
        print("Producto encontrado:", productos[indice], "-", cantidades[indice])


def modificar_cantidad():
    nombre = input("Nombre del producto a modificar: ").strip()
    indice = buscar_indice(nombre)
    if indice == -1:
        print("El producto no existe en el inventario.")
    else:
        print("Cantidad actual de", productos[indice], ":", cantidades[indice])
        cantidades[indice] = leer_cantidad("Nueva cantidad: ")
        print("Cantidad actualizada.")


def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ").strip()
    indice = buscar_indice(nombre)
    if indice == -1:
        print("El producto no existe en el inventario.")
    else:
        eliminado = productos.pop(indice)
        cantidades.pop(indice)
        print("Producto eliminado:", eliminado)


def mostrar_resumen():
    print("Productos diferentes registrados:", len(productos))


def mostrar_mayor_cantidad():
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        indice_mayor = 0
        for i in range(len(cantidades)):
            if cantidades[i] > cantidades[indice_mayor]:
                indice_mayor = i
        print("Producto con mayor cantidad:", productos[indice_mayor],
              "-", cantidades[indice_mayor])


def mostrar_menu():
    print("\n===== GESTOR DE INVENTARIO =====")
    print("1. Registrar un producto")
    print("2. Mostrar inventario")
    print("3. Buscar un producto")
    print("4. Modificar cantidad de un producto")
    print("5. Eliminar un producto")
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
            print("Opcion no valida. Elija un numero del 1 al 8.")


main()
