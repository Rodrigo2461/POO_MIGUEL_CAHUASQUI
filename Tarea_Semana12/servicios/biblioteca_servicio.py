# Realizado por: Miguel Cahuasqui
# Semana 12 - POO
from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:
    """Gestiona toda la lógica de negocio de la biblioteca digital."""
    
    def __init__(self):
        # REQUISITO TÉCNICO: Diccionario con clave ISBN y valor Objeto Libro
        self._libros_disponibles: dict[str, Libro] = {}
        
        # REQUISITO TÉCNICO: Conjunto (set) para gestionar IDs únicos rápidamente
        self._ids_usuarios: set[str] = set()
        
        # Diccionario extra para acceder rápido a los objetos Usuario
        self._usuarios: dict[str, Usuario] = {}

    # --- GESTIÓN DE LIBROS ---
    def anadir_libro(self, libro: Libro) -> str:
        if libro.isbn in self._libros_disponibles:
            return f"Error: El ISBN {libro.isbn} ya existe en el catálogo."
        self._libros_disponibles[libro.isbn] = libro
        return f"Éxito: Libro '{libro.get_titulo()}' añadido al catálogo."

    def quitar_libro(self, isbn: str) -> str:
        if isbn in self._libros_disponibles:
            del self._libros_disponibles[isbn]
            return "Éxito: Libro eliminado del catálogo."
        return "Error: Libro no encontrado en el inventario disponible."

    # --- GESTIÓN DE USUARIOS ---
    def registrar_usuario(self, usuario: Usuario) -> str:
        if usuario.id_usuario in self._ids_usuarios:
            return "Error: ID de usuario ya registrado."
        self._ids_usuarios.add(usuario.id_usuario)
        self._usuarios[usuario.id_usuario] = usuario
        return f"Éxito: Usuario '{usuario.nombre}' registrado correctamente."

    def dar_baja_usuario(self, id_usuario: str) -> str:
        if id_usuario not in self._ids_usuarios:
            return "Error: Usuario no encontrado."
        
        # Lógica de negocio: No dar de baja si tiene libros pendientes
        if len(self._usuarios[id_usuario].get_libros_prestados()) > 0:
            return "Error: El usuario debe devolver todos los libros antes de darse de baja."
        
        self._ids_usuarios.remove(id_usuario)
        del self._usuarios[id_usuario]
        return "Éxito: Usuario dado de baja del sistema."

    # --- PRÉSTAMOS Y DEVOLUCIONES ---
    def prestar_libro(self, id_usuario: str, isbn: str) -> str:
        if id_usuario not in self._ids_usuarios:
            return "Error: El usuario no existe."
        if isbn not in self._libros_disponibles:
            return "Error: El libro no está disponible (no existe o ya fue prestado)."

        # .pop() saca el libro del catálogo disponible para entregarlo al usuario
        libro_a_prestar = self._libros_disponibles.pop(isbn)
        self._usuarios[id_usuario].prestar_libro(libro_a_prestar)
        return f"Éxito: Libro prestado a {self._usuarios[id_usuario].nombre}."

    def devolver_libro(self, id_usuario: str, isbn: str) -> str:
        if id_usuario not in self._ids_usuarios:
            return "Error: El usuario no existe."

        libro_devuelto = self._usuarios[id_usuario].devolver_libro(isbn)
        if libro_devuelto:
            # Se reingresa el libro al catálogo de disponibles
            self._libros_disponibles[isbn] = libro_devuelto
            return f"Éxito: Libro '{libro_devuelto.get_titulo()}' devuelto a la biblioteca."
        return "Error: El usuario no tiene asignado un libro con ese ISBN."

    # --- BÚSQUEDAS ---
    def buscar_libros(self, criterio: str, valor_busqueda: str) -> list[Libro]:
        """Busca iterando sobre los valores del diccionario de libros."""
        resultados = []
        valor_busqueda = valor_busqueda.lower()
        
        for libro in self._libros_disponibles.values():
            if criterio == "titulo" and valor_busqueda in libro.get_titulo().lower():
                resultados.append(libro)
            elif criterio == "autor" and valor_busqueda in libro.get_autor().lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor_busqueda in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_prestados(self, id_usuario: str) -> list[Libro]:
        if id_usuario in self._usuarios:
            return self._usuarios[id_usuario].get_libros_prestados()
        return []