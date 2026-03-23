# TS14 PROGRAMACION ORIENTADA A OBJETOS
# Realizado por: Miguel Cahuasqui
# Descripción: Define la estructura de datos (Data Class) para un visitante.

class Visitante:
    """
    Clase que representa a un visitante de la oficina.
    Actúa como un modelo de datos puro (sin lógica de negocio).
    """

    def __init__(self, cedula: str, nombre: str, motivo: str) -> None:
        """
        Constructor del visitante.

        Parámetros:
            cedula (str): Número de cédula único que identifica al visitante.
            nombre (str): Nombre completo del visitante.
            motivo (str): Razón o motivo de la visita a la oficina.
        """
        # Identificador único del visitante
        self.cedula: str = cedula

        # Nombre completo del visitante
        self.nombre: str = nombre

        # Motivo o razón de la visita
        self.motivo: str = motivo

    def __str__(self) -> str:
        """
        Representación legible del objeto Visitante.
        Útil para depuración o impresión en consola.

        Retorna:
            str: Cadena con los datos principales del visitante.
        """
        return f"Visitante(cédula={self.cedula}, nombre={self.nombre}, motivo={self.motivo})"