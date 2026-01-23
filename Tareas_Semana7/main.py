from modelos.reporte import ReporteArchivo
from servicios.gestor_reportes import GestorReportes

def main():
    print("--- INICIO DE LA APLICACIÓN ---")
    
    # 1. Creación de instancia (Ejecuta __init__)
    # Pasamos los tipos de datos exactos: str, str, float
    mi_reporte = ReporteArchivo("Balance_Anual", "pdf", 1024.5)
    
    # 2. Uso del servicio
    gestor = GestorReportes("Miguel Cahuasqui")
    gestor.generar_resumen(mi_reporte)
    
    print("\n--- FINALIZANDO PROCESOS ---")
    
    # 3. Al terminar la función o usar 'del', se dispara el destructor
    # Forzamos la eliminación para ver el mensaje antes del fin del programa
    del mi_reporte 

if __name__ == "__main__":
    main()
    print("--- PROGRAMA TERMINADO TOTALMENTE ---")