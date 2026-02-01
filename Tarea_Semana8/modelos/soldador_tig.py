from modelos.soldador import Soldador

class SoldadorTIG(Soldador):

    def __init__(self, nombre: str, edad: int, experiencia: float, material: str):
        super().__init__(nombre, edad, experiencia)
        self.material = material

    # Polimorfismo
    def tipo_trabajo(self) -> str:
        return f"Soldadura TIG para material {self.material}"
