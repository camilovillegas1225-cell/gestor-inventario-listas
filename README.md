# Gestor de inventario con listas

## Objetivo

Programa de consola en Python que permite a una tienda pequeña administrar los nombres y las cantidades disponibles de sus productos, practicando el manejo de listas, índices, ciclos, condicionales y funciones.

## Requisitos para ejecutar

- Python 3 instalado.
- No requiere librerías externas, archivos ni bases de datos.

## Instrucciones de uso

1. Descargue o clone el repositorio.
2. Abra una terminal en la carpeta del proyecto.
3. Ejecute:

```
python main.py
```

4. Elija una opción del menú escribiendo su número y presionando Enter.

Los datos se guardan solo mientras el programa está abierto; se pierden al cerrarlo.

## Funciones implementadas

| Opción | Función | Descripción |
|---|---|---|
| 1 | `registrar_producto()` | Registra un producto y su cantidad disponible. |
| 2 | `mostrar_inventario()` | Muestra todos los productos con su cantidad. |
| 3 | `buscar_producto()` | Busca un producto por su nombre. |
| 4 | `modificar_cantidad()` | Modifica la cantidad de un producto existente. |
| 5 | `eliminar_producto()` | Elimina un producto existente. |
| 6 | `mostrar_resumen()` | Muestra cuántos productos diferentes hay registrados. |
| 7 | `mostrar_mayor_cantidad()` | Muestra el producto con mayor cantidad disponible. |
| 8 | — | Sale del programa. |

Funciones de apoyo: `leer_cantidad()` (valida que la cantidad sea un entero no negativo), `buscar_indice()` (devuelve la posición de un producto o -1 si no existe) y `mostrar_menu()`.

## Cómo se usan las listas

El programa usa dos listas paralelas: `productos` y `cantidades`. El elemento en el índice `i` de cada lista corresponde al mismo producto. Por ejemplo, `productos[0]` y `cantidades[0]` describen el mismo producto. Al eliminar, se quita el mismo índice en ambas listas para que sigan sincronizadas.

## Decisión sobre productos repetidos

No se permite registrar dos veces el mismo producto (sin distinguir mayúsculas de minúsculas). Así cada nombre tiene una sola cantidad y las listas paralelas se mantienen consistentes. Para cambiar la cantidad de un producto ya registrado se usa la opción 4.

## Manejo de casos límite

- Opciones de menú inexistentes muestran un mensaje claro.
- Buscar, modificar o eliminar un producto que no existe muestra un aviso.
- Inventario vacío muestra un aviso en lugar de fallar.
- Las cantidades no numéricas o negativas se rechazan y se vuelven a pedir.

## Autor

Nombre completo y grupo del estudiante.
