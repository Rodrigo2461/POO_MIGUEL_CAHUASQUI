from typing import Dict


class Producto:
    """
    Modelo de Producto.
    Representa una entidad del inventario.
    """

    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float) -> None:
        self._id: str = id_producto
        self._nombre: str = nombre
        self._cantidad: int = cantidad
        self._precio: float = precio

    # Getters
    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_cantidad(self) -> int:
        return self._cantidad

    def get_precio(self) -> float:
        return self._precio

    # Setters
    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def set_cantidad(self, cantidad: int) -> None:
        self._cantidad = cantidad

    def set_precio(self, precio: float) -> None:
        self._precio = precio

    def to_linea_archivo(self) -> str:
        """
        Convierte el producto a línea de texto para archivo.
        """
        return f"{self._id},{self._nombre},{self._cantidad},{self._precio}\n"

    @staticmethod
    def desde_linea(linea: str) -> "Producto":
        """
        Crea un producto desde una línea del archivo.
        Lanza ValueError si el formato es inválido.
        """
        partes: list[str] = linea.strip().split(",")

        if len(partes) != 4:
            raise ValueError("Línea de archivo corrupta")

        id_p: str = partes[0]
        nombre: str = partes[1]
        cantidad: int = int(partes[2])
        precio: float = float(partes[3])

        return Producto(id_p, nombre, cantidad, precio)