# hecho por Miguel Cahuasqui

from modelos.producto import Producto
from servicios.inventario import Inventario

#--------------------

def pedir_entero(mensaje: str) -> int:
    # Lee un entero desde teclado (str) -> int
    while True:
        try:
            return int(input(mensaje))
        except:
            print("Numero invalido")

#--------------------

def pedir_float(mensaje: str) -> float:
    # Lee un decimal desde teclado (str) -> float
    while True:
        try:
            return float(input(mensaje))
        except:
            print("Numero invalido")

#--------------------

def menu() -> None:
    # Muestra el menu de opciones -> None
    print("""
SISTEMA INVENTARIO
1 Añadir producto
2 Eliminar producto
3 Actualizar producto
4 Buscar producto
5 Listar inventario
6 Salir
""")

#--------------------

def main() -> None:
    # Punto de inicio del sistema -> None

    inventario: Inventario = Inventario()

    while True:
        menu()
        opcion: str = input("Opcion: ")

        #--------------------

        if opcion == "1":
            idp: int = pedir_entero("ID: ")
            nombre: str = input("Nombre: ")
            cantidad: int = pedir_entero("Cantidad: ")
            precio: float = pedir_float("Precio: ")

            producto: Producto = Producto(idp, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        #--------------------

        elif opcion == "2":
            idp: int = pedir_entero("ID a eliminar: ")
            inventario.eliminar_producto(idp)

        #--------------------

        elif opcion == "3":
            idp: int = pedir_entero("ID a actualizar: ")
            cantidad: int = pedir_entero("Nueva cantidad (-1 no cambia): ")
            precio: float = pedir_float("Nuevo precio (-1 no cambia): ")

            nueva_cant: int | None = None if cantidad == -1 else cantidad
            nuevo_precio: float | None = None if precio == -1 else precio

            inventario.actualizar_producto(idp, nueva_cant, nuevo_precio)

        #--------------------

        elif opcion == "4":
            texto: str = input("Buscar: ")
            resultados: list[Producto] = inventario.buscar_por_nombre(texto)

            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("Sin resultados")

        #--------------------

        elif opcion == "5":
            inventario.mostrar_todos()

        #--------------------

        elif opcion == "6":
            break

        else:
            print("Opcion invalida")

#--------------------

if __name__ == "__main__":
    main()
