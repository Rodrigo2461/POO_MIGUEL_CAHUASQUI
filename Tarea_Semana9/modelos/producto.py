# hecho por Miguel Cahuasqui

class Producto:
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        # Constructor: crea un producto con id int, nombre str, cantidad int y precio float
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    #--------------------

    def get_id(self) -> int:
        # Devuelve el id del producto (int)
        return self._id

    def get_nombre(self) -> str:
        # Devuelve el nombre del producto (str)
        return self._nombre

    def get_cantidad(self) -> int:
        # Devuelve la cantidad en inventario (int)
        return self._cantidad

    def get_precio(self) -> float:
        # Devuelve el precio del producto (float)
        return self._precio

    #--------------------

    def set_nombre(self, nombre: str) -> None:
        # Actualiza el nombre del producto (str)
        self._nombre = nombre

    def set_cantidad(self, cantidad: int) -> None:
        # Actualiza la cantidad si es >= 0 (int)
        if cantidad >= 0:
            self._cantidad = cantidad

    def set_precio(self, precio: float) -> None:
        # Actualiza el precio si es >= 0 (float)
        if precio >= 0:
            self._precio = precio

    #--------------------

    def __str__(self) -> str:
        # Devuelve representación en texto del producto (str)
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"
