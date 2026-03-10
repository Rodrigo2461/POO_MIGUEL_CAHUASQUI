# Realizado por: Miguel Cahuasqui
# Semana 13 - POO

from modelos.vehiculo import Vehiculo

class GarajeServicio:
    """Gestiona la lógica de almacenamiento de los vehículos."""
    
    def __init__(self):
        # Lista para almacenar los objetos Vehiculo
        self._vehiculos: list[Vehiculo] = []

    def agregar_vehiculo(self, vehiculo: Vehiculo) -> bool:
        """Añade un vehículo a la lista si la placa no está registrada."""
        # Validación básica para no duplicar placas
        for v in self._vehiculos:
            if v.placa == vehiculo.placa:
                return False
        self._vehiculos.append(vehiculo)
        return True

    def obtener_vehiculos(self) -> list[Vehiculo]:
        """Retorna la lista completa de vehículos registrados."""
        return self._vehiculos