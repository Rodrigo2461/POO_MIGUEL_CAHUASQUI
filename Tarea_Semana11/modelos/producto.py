class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.
        Define los atributos con tipos de datos estrictos (str, int, float).
        """
        self.id_producto: str = id_producto
        self.nombre: str = nombre
        self.cantidad: int = cantidad
        self.precio: float = precio

    # Métodos para establecer (setters) nuevos valores
    def set_cantidad(self, nueva_cantidad: int):
        """Actualiza la cantidad del producto."""
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio: float):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio

    def obtener_info(self) -> str:
        """Devuelve una cadena de texto con la información del producto."""
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"