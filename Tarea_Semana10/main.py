from modelos.producto import Producto
from servicios.inventario import Inventario
"""
HECHO POR MIGUEL CAHUASQUI
PROGRAMACIÓN ORIENTADA A OBJETOS
TAREA SEMANA 10
SISTEMA DE GESTIÓN DE INVENTARIOS MEJORADO CON ARCHIVOS Y MANEJO DE EXCEPCIONES
"""

def leer_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese número entero válido")


def leer_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingrese número decimal válido")


def main() -> None:
    inv: Inventario = Inventario()

    while True:
        print("\n1 Agregar")
        print("2 Actualizar")
        print("3 Eliminar")
        print("4 Buscar")
        print("5 Listar")
        print("0 Salir")

        op: str = input("Opción: ")

        if op == "1":
            id_p: str = input("ID: ")
            nombre: str = input("Nombre: ")
            cantidad: int = leer_entero("Cantidad: ")
            precio: float = leer_float("Precio: ")

            prod: Producto = Producto(id_p, nombre, cantidad, precio)
            inv.agregar(prod)

        elif op == "2":
            id_p = input("ID: ")
            cantidad = leer_entero("Nueva cantidad: ")
            precio = leer_float("Nuevo precio: ")
            inv.actualizar(id_p, cantidad, precio)

        elif op == "3":
            inv.eliminar(input("ID: "))

        elif op == "4":
            p = inv.buscar(input("ID: "))
            if p:
                print(p.get_id(), p.get_nombre(), p.get_cantidad(), p.get_precio())
            else:
                print("No encontrado")

        elif op == "5":
            inv.listar()

        elif op == "0":
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()