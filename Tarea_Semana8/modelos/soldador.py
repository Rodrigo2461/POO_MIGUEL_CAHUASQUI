# modelos/soldador.py

class Soldador:
    """
    Clase base Soldador
    Realizado por Miguel Cahuásqui
    """

    def __init__(self, nombre: str, edad: int, experiencia: float):
        # Encapsulamiento (atributos privados)
        self.__nombre = nombre
        self.__edad = edad
        self.__experiencia = experiencia

        print(f"Constructor Soldador ejecutado -> {self.__nombre}")

    # Destructor
    def __del__(self):
        print(f"Destructor Soldador ejecutado -> {self.__nombre}")

    # GETTERS
    def get_nombre(self) -> str:
        return self.__nombre

    def get_edad(self) -> int:
        return self.__edad

    def get_experiencia(self) -> float:
        return self.__experiencia

    # SETTERS
    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_edad(self, edad: int):
        if edad > 0:
            self.__edad = edad

    def set_experiencia(self, experiencia: float):
        if experiencia >= 0:
            self.__experiencia = experiencia

    # Método que será polimórfico
    def tipo_trabajo(self) -> str:
        return "Trabajo general de soldadura"
