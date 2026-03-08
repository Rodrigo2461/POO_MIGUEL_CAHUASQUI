# Realizado por: Miguel Cahuasqui
# Semana 12 - POO

class Libro:
    """Clase que representa la entidad de un Libro."""
    
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        # REQUISITO TÉCNICO: Uso de tupla inmutable para título y autor.
        # Encapsulado como protegido (_) para que no se modifique desde fuera.
        self._info_basica: tuple[str, str] = (titulo, autor)
        self.categoria: str = categoria
        self.isbn: str = isbn

    # Métodos de acceso (Getters) para leer los datos de la tupla
    def get_titulo(self) -> str:
        return self._info_basica[0]

    def get_autor(self) -> str:
        return self._info_basica[1]

    def __str__(self) -> str:
        # Formato de impresión amigable
        return f"[{self.isbn}] '{self.get_titulo()}' por {self.get_autor()} ({self.categoria})"