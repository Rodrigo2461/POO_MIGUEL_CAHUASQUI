# Archivo: modelos/soldador.py
# Contiene la clase Soldador que representa a un trabajador

class Soldador:
    
    # Constructor: inicializa los atributos del soldador
    def __init__(self, nombre, cedula, experiencia):
        # Atributo publico
        self.nombre = nombre
        
        # Atributos privados con __
        # ENCAPSULACION: protegemos datos sensibles como la cedula
        self.__cedula = cedula
        self.__experiencia = experiencia
        
        # Contador de trabajos realizados
        self.trabajos_completados = 0
    
    # Metodo getter: obtiene la cedula de forma segura
    # ENCAPSULACION: mostramos solo parte de la cedula por seguridad
    def obtener_cedula(self):
        # Muestra solo los ultimos 4 digitos
        return "****" + self.__cedula[-4:]
    
    # Metodo getter para la experiencia
    def obtener_experiencia(self):
        return self.__experiencia
    
    # Metodo setter: modifica la experiencia con validacion
    # ENCAPSULACION: validamos que los datos sean correctos
    def establecer_experiencia(self, nueva_experiencia):
        if nueva_experiencia >= 0:
            self.__experiencia = nueva_experiencia
            print("Experiencia actualizada a " + str(nueva_experiencia) + " años")
        else:
            print("Error: La experiencia no puede ser negativa")
    
    # Metodo para registrar un trabajo completado
    def registrar_trabajo(self):
        self.trabajos_completados = self.trabajos_completados + 1
        print("Trabajo registrado. Total: " + str(self.trabajos_completados))
    
    # Metodo para mostrar informacion del soldador
    def mostrar_info(self):
        print("Nombre: " + self.nombre)
        print("Cedula: " + self.obtener_cedula())
        print("Experiencia: " + str(self.__experiencia) + " años")
        print("Trabajos completados: " + str(self.trabajos_completados))