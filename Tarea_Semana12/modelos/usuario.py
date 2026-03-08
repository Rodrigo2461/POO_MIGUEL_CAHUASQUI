# Realizado por: Miguel Cahuasqui
# Semana 12 - POO
from modelos.libro import Libro

class Usuario:
    """Clase que representa a un usuario registrado en la biblioteca."""
    
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre: str = nombre
        self.id_usuario: str = id_usuario
        # REQUISITO TÉCNICO: Uso de lista para almacenar libros prestados.
        # Atributo protegido para aplicar encapsulamiento.
        self._libros_prestados: list[Libro] = []

    def prestar_libro(self, libro: Libro):
        """Añade un objeto Libro a la lista del usuario."""
        self._libros_prestados.append(libro)

    def devolver_libro(self, isbn: str) -> Libro | None:
        """Busca el libro por ISBN, lo saca de la lista y lo retorna."""
        for libro in self._libros_prestados:
            if libro.isbn == isbn:
                self._libros_prestados.remove(libro)
                return libro
        return None

    def get_libros_prestados(self) -> list[Libro]:
        """Retorna la lista de libros actualmente prestados."""
        return self._libros_prestados