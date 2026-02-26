import json
import os
from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo_datos: str = "inventario.json"):
        """
        Constructor del Inventario.
        Inicializa el diccionario (colección) y carga los datos del archivo.
        """
        self.archivo_datos: str = archivo_datos
        self.productos: dict = {}  # Diccionario para almacenar los productos (ID como clave)
        self.cargar_desde_archivo()

    def añadir_producto(self, producto: Producto):
        """Añade un producto si el ID no existe en el diccionario."""
        if producto.id_producto in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto: str):
        """Elimina un producto del diccionario usando su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto: str, nueva_cantidad: int = None, nuevo_precio: float = None):
        """Actualiza la cantidad o el precio de un producto existente."""
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].set_precio(nuevo_precio)
            self.guardar_en_archivo()
            print("Producto actualizado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre: str):
        """Busca y muestra productos que coincidan con el nombre (usando listas)."""
        encontrados = []
        # Recorremos los valores del diccionario
        for prod in self.productos.values():
            if prod.nombre.lower() == nombre.lower():
                encontrados.append(prod)
        
        if encontrados:
            for p in encontrados:
                print(p.obtener_info())
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for prod in self.productos.values():
                print(prod.obtener_info())

    # --- Manejo de Archivos ---
    def guardar_en_archivo(self):
        """Serializa el diccionario de productos y lo guarda en un archivo JSON."""
        datos_a_guardar = {}
        for id_prod, prod in self.productos.items():
            # Convertimos el objeto a un formato de diccionario simple para JSON
            datos_a_guardar[id_prod] = {
                "nombre": prod.nombre,
                "cantidad": prod.cantidad,
                "precio": prod.precio
            }
        
        with open(self.archivo_datos, 'w') as archivo:
            json.dump(datos_a_guardar, archivo, indent=4)

    def cargar_desde_archivo(self):
        """Deserializa el archivo JSON y reconstruye el diccionario de objetos Producto."""
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r') as archivo:
                    datos_cargados = json.load(archivo)
                    
                    # Reconstruimos los objetos Producto a partir del archivo
                    for id_prod, datos in datos_cargados.items():
                        nuevo_producto = Producto(id_prod, datos["nombre"], datos["cantidad"], datos["precio"])
                        self.productos[id_prod] = nuevo_producto
            except json.JSONDecodeError:
                print("El archivo de datos está vacío o corrupto. Se iniciará un inventario nuevo.")