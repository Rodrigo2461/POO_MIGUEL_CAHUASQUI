# Realizado por: Miguel Cahuasqui
# Semana 12 - POO
from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio

def mostrar_menu():
    """Interfaz visual en consola, sin lógica de negocio."""
    print("\n" + "="*40)
    print("   BIBLIOTECA DIGITAL - MIGUEL CAHUASQUI   ")
    print("="*40)
    print("1. Añadir libro al catálogo")
    print("2. Quitar libro del catálogo")
    print("3. Registrar nuevo usuario")
    print("4. Dar de baja a un usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros")
    print("8. Listar libros prestados a un usuario")
    print("0. Salir")
    return input("\n> Seleccione una opción: ")

def main():
    # Instanciamos la clase de servicio
    biblioteca = BibliotecaServicio()
    
    # Datos de prueba para facilitar la demostración al profesor
    biblioteca.anadir_libro(Libro("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", "ISBN001"))
    biblioteca.anadir_libro(Libro("1984", "George Orwell", "Ficción", "ISBN002"))
    biblioteca.registrar_usuario(Usuario("Carlos Ruiz", "USER100"))

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            cat = input("Categoría: ")
            isbn = input("ISBN: ")
            print(biblioteca.anadir_libro(Libro(titulo, autor, cat, isbn)))

        elif opcion == '2':
            isbn = input("ISBN del libro a eliminar: ")
            print(biblioteca.quitar_libro(isbn))

        elif opcion == '3':
            nombre = input("Nombre del usuario: ")
            id_usr = input("ID de usuario (único): ")
            print(biblioteca.registrar_usuario(Usuario(nombre, id_usr)))

        elif opcion == '4':
            id_usr = input("ID de usuario a dar de baja: ")
            print(biblioteca.dar_baja_usuario(id_usr))

        elif opcion == '5':
            id_usr = input("ID del usuario que solicita: ")
            isbn = input("ISBN del libro a prestar: ")
            print(biblioteca.prestar_libro(id_usr, isbn))

        elif opcion == '6':
            id_usr = input("ID del usuario que devuelve: ")
            isbn = input("ISBN del libro a devolver: ")
            print(biblioteca.devolver_libro(id_usr, isbn))

        elif opcion == '7':
            print("Criterios válidos: titulo, autor, categoria")
            criterio = input("Buscar por: ").lower()
            if criterio in ['titulo', 'autor', 'categoria']:
                valor = input("Término a buscar: ")
                resultados = biblioteca.buscar_libros(criterio, valor)
                if resultados:
                    print("\n--- Resultados de la Búsqueda ---")
                    for r in resultados:
                        print(r)
                else:
                    print("\nNo se encontraron coincidencias.")
            else:
                print("Criterio inválido.")

        elif opcion == '8':
            id_usr = input("ID del usuario: ")
            prestados = biblioteca.listar_prestados(id_usr)
            if prestados:
                print(f"\n--- Libros en poder de {id_usr} ---")
                for p in prestados:
                    print(p)
            else:
                print("\nEl usuario no tiene libros prestados o no existe.")

        elif opcion == '0':
            print("Cerrando el sistema... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()