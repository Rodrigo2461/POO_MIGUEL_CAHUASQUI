import os

class ReporteArchivo:
    def __init__(self, nombre_archivo: str, extension: str, tamaño_kb: float):
        """
        Constructor (__init__): Inicializa el estado del objeto.
        Se han definido tipos de datos explícitos para corregir observaciones previas.
        """
        # Atributos con tipado explícito
        self.nombre_archivo: str = nombre_archivo
        self.extension: str = extension
        self.tamaño_kb: float = tamaño_kb
        self.archivo_abierto: bool = False
        
        # Simulación de apertura de un recurso
        self.archivo_abierto = True
        print(f"[Modelo]: Objeto '{self.nombre_archivo}.{self.extension}' creado y recurso reservado.")

    def __del__(self):
        """
        Destructor (__del__): Se encarga de la limpieza.
        Es vital para cerrar flujos de datos o archivos que quedaron abiertos en memoria.
        """
        if self.archivo_abierto:
            self.archivo_abierto = False
            print(f"[Modelo]: Destructor ejecutado. El archivo '{self.nombre_archivo}' ha sido cerrado correctamente.")
        else:
            print(f"[Modelo]: Destructor ejecutado. No había recursos pendientes por liberar.")