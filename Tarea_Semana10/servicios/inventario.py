from typing import Dict
from modelos.producto import Producto
import os


class Inventario:
    """
    Servicio de Inventario.
    Maneja lógica de negocio y persistencia en archivo.
    """

    def __init__(self, ruta_archivo: str = "inventario.txt") -> None:
        self._ruta: str = ruta_archivo
        self._productos: Dict[str, Producto] = {}
        self._cargar_archivo()

    # -------------------------
    # Carga inicial desde archivo
    # -------------------------
    def _cargar_archivo(self) -> None:
        """
        Carga productos desde archivo.
        Crea archivo si no existe.
        Maneja errores de lectura y formato.
        """
        try:
            if not os.path.exists(self._ruta):
                open(self._ruta, "w").close()

            with open(self._ruta, "r", encoding="utf-8") as f:
                for linea in f:
                    if linea.strip() == "":
                        continue
                    try:
                        producto: Producto = Producto.desde_linea(linea)
                        self._productos[producto.get_id()] = producto
                    except ValueError:
                        print("Línea inválida ignorada en archivo")

        except PermissionError:
            print("Error: sin permisos para leer archivo")

        except OSError as e:
            print(f"Error de sistema al leer archivo: {e}")

    # -------------------------
    # Guardar todo el inventario
    # -------------------------
    def _guardar_archivo(self) -> bool:
        """
        Reescribe el archivo completo.
        Retorna True si éxito, False si falla.
        """
        try:
            with open(self._ruta, "w", encoding="utf-8") as f:
                for prod in self._productos.values():
                    f.write(prod.to_linea_archivo())
            return True

        except PermissionError:
            print("Error: sin permisos de escritura")
            return False

        except OSError as e:
            print(f"Error de sistema al guardar: {e}")
            return False

    # -------------------------
    # Operaciones CRUD
    # -------------------------
    def agregar(self, producto: Producto) -> bool:
        if producto.get_id() in self._productos:
            print("ID ya existe")
            return False

        self._productos[producto.get_id()] = producto
        ok: bool = self._guardar_archivo()

        if ok:
            print("Producto agregado y guardado")
        return ok

    def actualizar(self, id_p: str, cantidad: int, precio: float) -> bool:
        prod: Producto | None = self._productos.get(id_p)

        if prod is None:
            print("Producto no encontrado")
            return False

        prod.set_cantidad(cantidad)
        prod.set_precio(precio)

        ok: bool = self._guardar_archivo()
        if ok:
            print("Producto actualizado en archivo")
        return ok

    def eliminar(self, id_p: str) -> bool:
        if id_p not in self._productos:
            print("Producto no existe")
            return False

        del self._productos[id_p]

        ok: bool = self._guardar_archivo()
        if ok:
            print("Producto eliminado del archivo")
        return ok

    def buscar(self, id_p: str) -> Producto | None:
        return self._productos.get(id_p)

    def listar(self) -> None:
        for p in self._productos.values():
            print(
                p.get_id(),
                p.get_nombre(),
                p.get_cantidad(),
                p.get_precio()
            )