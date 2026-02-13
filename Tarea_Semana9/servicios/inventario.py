# hecho por Miguel Cahuasqui

from modelos.producto import Producto

class Inventario:

    def __init__(self):
        # Lista principal de almacenamiento de objetos Producto (list[Producto])
        self.productos: list[Producto] = []

    #--------------------

    def añadir_producto(self, producto: Producto) -> bool:
        # Agrega un producto si el id no está repetido (Producto) -> bool
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("ID ya existe")
                return False

        self.productos.append(producto)
        print("Producto añadido")
        return True

    #--------------------

    def eliminar_producto(self, id_producto: int) -> bool:
        # Elimina un producto por id (int) -> bool
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado")
                return True

        print("Producto no encontrado")
        return False

    #--------------------

    def actualizar_producto(
        self,
        id_producto: int,
        nueva_cantidad: int | None = None,
        nuevo_precio: float | None = None
    ) -> bool:
        # Actualiza cantidad y/o precio por id (int, int|None, float|None) -> bool
        for p in self.productos:
            if p.get_id() == id_producto:

                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                print("Producto actualizado")
                return True

        print("Producto no encontrado")
        return False

    #--------------------

    def buscar_por_nombre(self, texto: str) -> list[Producto]:
        # Busca productos por coincidencia parcial de nombre (str) -> list[Producto]
        resultados: list[Producto] = []

        for p in self.productos:
            if texto.lower() in p.get_nombre().lower():
                resultados.append(p)

        return resultados

    #--------------------

    def mostrar_todos(self) -> None:
        # Muestra todos los productos en consola -> None
        if not self.productos:
            print("Inventario vacio")
            return

        print("INVENTARIO")
        for p in self.productos:
            print(p)
