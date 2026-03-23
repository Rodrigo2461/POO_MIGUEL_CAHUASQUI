# TS14 PROGRAMACION ORIENTADA A OBJETOS
# Realizado por: Miguel Cahuasqui
# Descripción: Capa de lógica de negocio. Gestiona todas las operaciones
#              CRUD sobre la lista interna de visitantes en memoria.

from modelos.visitante import Visitante


class VisitaServicio:
    """
    Servicio encargado de gestionar los visitantes registrados.
    Encapsula la lista de visitantes y expone métodos CRUD claros.
    """

    def __init__(self) -> None:
        """
        Constructor del servicio.
        Inicializa la lista interna de visitantes vacía.
        El atributo es privado para respetar el principio de encapsulamiento.
        """
        # Lista privada que almacena los objetos Visitante en memoria
        self.__visitantes: list[Visitante] = []

    # ------------------------------------------------------------------
    # CREATE – Registrar un nuevo visitante
    # ------------------------------------------------------------------
    def registrar(self, cedula: str, nombre: str, motivo: str) -> tuple[bool, str]:
        """
        Crea un nuevo objeto Visitante y lo agrega a la lista interna,
        siempre que la cédula no esté ya registrada.

        Parámetros:
            cedula (str): Cédula del visitante (identificador único).
            nombre (str): Nombre completo del visitante.
            motivo (str): Motivo de la visita.

        Retorna:
            tuple[bool, str]: (éxito, mensaje descriptivo del resultado).
        """
        # Verificar si ya existe un visitante con la misma cédula
        if self.__buscar_por_cedula(cedula) is not None:
            return False, f"Ya existe un visitante registrado con la cédula '{cedula}'."

        # Instanciar y agregar el nuevo visitante
        nuevo: Visitante = Visitante(cedula, nombre, motivo)
        self.__visitantes.append(nuevo)
        return True, f"Visitante '{nombre}' registrado con éxito."

    # ------------------------------------------------------------------
    # READ – Obtener todos los visitantes
    # ------------------------------------------------------------------
    def obtener_todos(self) -> list[Visitante]:
        """
        Retorna una copia de la lista completa de visitantes registrados.
        Se entrega una copia para proteger el estado interno del servicio.

        Retorna:
            list[Visitante]: Lista con todos los visitantes actuales.
        """
        return list(self.__visitantes)

    # ------------------------------------------------------------------
    # DELETE – Eliminar un visitante por cédula
    # ------------------------------------------------------------------
    def eliminar(self, cedula: str) -> tuple[bool, str]:
        """
        Elimina de la lista al visitante cuya cédula coincida con el
        parámetro recibido.

        Parámetros:
            cedula (str): Cédula del visitante a eliminar.

        Retorna:
            tuple[bool, str]: (éxito, mensaje descriptivo del resultado).
        """
        visitante: Visitante | None = self.__buscar_por_cedula(cedula)

        if visitante is None:
            return False, f"No se encontró un visitante con la cédula '{cedula}'."

        self.__visitantes.remove(visitante)
        return True, f"Visitante con cédula '{cedula}' eliminado correctamente."

    # ------------------------------------------------------------------
    # Método privado auxiliar – Buscar por cédula
    # ------------------------------------------------------------------
    def __buscar_por_cedula(self, cedula: str) -> "Visitante | None":
        """
        Método interno que recorre la lista buscando un visitante
        que coincida con la cédula indicada.

        Parámetros:
            cedula (str): Cédula a buscar.

        Retorna:
            Visitante | None: El objeto encontrado, o None si no existe.
        """
        for visitante in self.__visitantes:
            if visitante.cedula == cedula:
                return visitante
        return None