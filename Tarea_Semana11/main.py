"""
Tarea Semana 11 
Programacion Orientada a Objetos
Hecho por Miguel Cahuasqui
"""

from modelos.producto import Producto
from servicios.inventario import Inventario

def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n--- SISTEMA AVANZADO DE GESTIÓN DE INVENTARIO ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("-------------------------------------------------")

def main():
    # Instanciamos el servicio (esto cargará los datos del archivo automáticamente)
    mi_inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_prod = input("Ingrese el ID del producto: ")
                nombre = input("Ingrese el nombre: ")
                cantidad = int(input("Ingrese la cantidad (número entero): "))
                precio = float(input("Ingrese el precio (número decimal): "))
                
                nuevo_prod = Producto(id_prod, nombre, cantidad, precio)
                mi_inventario.añadir_producto(nuevo_prod)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")

        elif opcion == '2':
            id_prod = input("Ingrese el ID del producto a eliminar: ")
            mi_inventario.eliminar_producto(id_prod)

        elif opcion == '3':
            id_prod = input("Ingrese el ID del producto a actualizar: ")
            
            # Pedimos nuevos datos. Si el usuario presiona Enter, no se actualiza ese campo.
            cant_input = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            prec_input = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            
            nueva_cantidad = int(cant_input) if cant_input else None
            nuevo_precio = float(prec_input) if prec_input else None
            
            mi_inventario.actualizar_producto(id_prod, nueva_cantidad, nuevo_precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            mi_inventario.buscar_por_nombre(nombre)

        elif opcion == '5':
            mi_inventario.mostrar_todos()

        elif opcion == '6':
            print("Guardando cambios y saliendo del sistema. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()