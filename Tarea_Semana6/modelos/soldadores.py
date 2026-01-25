# Realizado por: Miguel Cahuasqui
# Archivo: modelos/soldadores.py

class Soldador:
    """
    Clase Base que representa a un soldador genérico.
    """
    def __init__(self, nombre: str, id_empleado: int, especialidad: str):
        # Atributos públicos con tipos de datos definidos
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.especialidad = especialidad
        # ENCAPSULAMIENTO: Atributo protegido (inicia con un guion bajo)
        # Solo debe ser accedido o modificado dentro de la clase o subclases.
        self._horas_trabajadas: int = 0

    def registrar_horas(self, horas: int):
        """Método para modificar el atributo encapsulado."""
        if horas > 0:
            self._horas_trabajadas += horas
            print(f"Horas registradas para {self.nombre}: {horas}")
        else:
            print("La cantidad de horas debe ser positiva.")

    def realizar_soldadura(self):
        """Método base que será sobrescrito (POLIMORFISMO)."""
        print(f"{self.nombre} está realizando una soldadura general estándar.")

class SoldadorTIG(Soldador):
    """
    Clase Derivada (HERENCIA) que representa a un especialista en TIG.
    Hereda atributos y métodos de Soldador.
    """
    def __init__(self, nombre: str, id_empleado: int, certificacion_nivel: int):
        # Llamamos al constructor de la clase padre (super)
        super().__init__(nombre, id_empleado, "TIG (Tungsten Inert Gas)")
        self.certificacion_nivel = certificacion_nivel

    # POLIMORFISMO: Sobrescribimos el método de la clase padre
    # para dar un comportamiento específico.
    def realizar_soldadura(self):
        print(f"{self.nombre} (Nivel {self.certificacion_nivel}) está realizando una soldadura TIG de alta precisión en acero inoxidable.")