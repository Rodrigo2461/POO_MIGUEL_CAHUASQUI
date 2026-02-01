from modelos.soldador import Soldador

class SoldadorMIG(Soldador):

    def __init__(self, nombre: str, edad: int, experiencia: float, gas: str):
        super().__init__(nombre, edad, experiencia)
        self.gas = gas

    # Polimorfismo
    def tipo_trabajo(self) -> str:
        return f"Soldadura MIG usando gas {self.gas}"
