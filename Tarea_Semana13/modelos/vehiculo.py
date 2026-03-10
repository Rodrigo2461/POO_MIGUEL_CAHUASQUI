# Realizado por: Miguel Cahuasqui
# Semana 13 - POO

class Vehiculo:
    """Modelo que representa un vehículo en el garaje."""
    
    def __init__(self, placa: str, marca: str, propietario: str):
        # Atributos fuertemente tipados
        self.placa: str = placa
        self.marca: str = marca
        self.propietario: str = propietario