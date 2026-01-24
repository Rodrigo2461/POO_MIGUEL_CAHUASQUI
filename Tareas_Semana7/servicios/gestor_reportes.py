from modelos.reporte import ReporteArchivo

class GestorReportes:
    def __init__(self, administrador: str):
        # Tipado en el constructor del servicio también
        self.administrador: str = administrador
        print(f"[Servicio]: Gestor iniciado por el admin: {self.administrador}")

    def generar_resumen(self, reporte: ReporteArchivo) -> None:
        """Lógica para procesar la información del modelo."""
        print(f"[Servicio]: Procesando reporte '{reporte.nombre_archivo}'...")
        print(f"            - Tamaño detectado: {reporte.tamaño_kb} KB")
        print(f"            - Estado: {'Activo' if reporte.archivo_abierto else 'Inactivo'}")