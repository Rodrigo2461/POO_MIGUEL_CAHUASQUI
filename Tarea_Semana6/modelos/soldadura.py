# Archivo: modelos/soldadura.py
# Contiene las clases relacionadas con procesos de soldadura

# CLASE BASE
# Esta es la clase padre de la cual heredaran las demas clases
class Soldadura:
    
    # Constructor: se ejecuta cuando creamos un objeto de esta clase
    def __init__(self, tipo, amperaje, voltaje):
        # Atributos publicos: se pueden acceder desde fuera de la clase
        self.tipo = tipo
        
        # Atributos privados: tienen __ al inicio
        # ENCAPSULACION: protegemos estos datos para que no se modifiquen directamente
        self.__amperaje = amperaje
        self.__voltaje = voltaje
    
    # Metodo getter: permite obtener el valor del amperaje de forma controlada
    def obtener_amperaje(self):
        return self.__amperaje
    
    # Metodo setter: permite modificar el amperaje con validacion
    # ENCAPSULACION: validamos que el valor sea correcto antes de guardarlo
    def establecer_amperaje(self, nuevo_amperaje):
        if nuevo_amperaje > 0:
            self.__amperaje = nuevo_amperaje
        else:
            print("Error: El amperaje debe ser mayor a 0")
    
    # Metodo getter para voltaje
    def obtener_voltaje(self):
        return self.__voltaje
    
    # Metodo setter para voltaje con validacion
    def establecer_voltaje(self, nuevo_voltaje):
        if nuevo_voltaje > 0:
            self.__voltaje = nuevo_voltaje
        else:
            print("Error: El voltaje debe ser mayor a 0")
    
    # Metodo para calcular la potencia electrica (P = V * I)
    def calcular_potencia(self):
        return self.__voltaje * self.__amperaje
    
    # Este metodo sera sobrescrito en las clases hijas
    # POLIMORFISMO: mismo metodo, diferentes comportamientos
    def iniciar(self):
        return "Iniciando soldadura tipo " + self.tipo
    
    # Metodo para mostrar informacion del proceso
    def mostrar_info(self):
        return "Tipo: " + self.tipo + "\nAmperaje: " + str(self.__amperaje) + " A\nVoltaje: " + str(self.__voltaje) + " V"


# CLASE DERIVADA 1: Hereda de Soldadura
# HERENCIA: SoldaduraMIG es hija de Soldadura
class SoldaduraMIG(Soldadura):
    
    # Constructor de la clase hija
    def __init__(self, amperaje, voltaje, gas):
        # super() llama al constructor de la clase padre
        # HERENCIA: reutilizamos el codigo de la clase padre
        super().__init__("MIG", amperaje, voltaje)
        
        # Atributo especifico de esta clase
        self.gas = gas
    
    # Sobrescribimos el metodo iniciar de la clase padre
    # POLIMORFISMO: mismo nombre de metodo pero comportamiento diferente
    def iniciar(self):
        return "Iniciando soldadura MIG\nGas protector: " + self.gas + "\nAmperaje: " + str(self.obtener_amperaje()) + " A"
    
    # Metodo especifico de esta clase
    def cambiar_gas(self, nuevo_gas):
        self.gas = nuevo_gas
        print("Gas cambiado a: " + nuevo_gas)


# CLASE DERIVADA 2: Tambien hereda de Soldadura
# HERENCIA: SoldaduraTIG es hija de Soldadura
class SoldaduraTIG(Soldadura):
    
    # Constructor de la clase hija
    def __init__(self, amperaje, voltaje, electrodo):
        # Llamamos al constructor del padre con super()
        super().__init__("TIG", amperaje, voltaje)
        
        # Atributo especifico de TIG
        self.electrodo = electrodo
    
    # Sobrescribimos el metodo iniciar
    # POLIMORFISMO: mismo metodo que en MIG pero comportamiento distinto
    def iniciar(self):
        return "Iniciando soldadura TIG\nElectrodo: " + self.electrodo + "\nAmperaje: " + str(self.obtener_amperaje()) + " A"
    
    # Metodo especifico de esta clase
    def cambiar_electrodo(self, nuevo_electrodo):
        self.electrodo = nuevo_electrodo
        print("Electrodo cambiado a: " + nuevo_electrodo)