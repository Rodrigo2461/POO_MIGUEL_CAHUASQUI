# Realizado por: Miguel Cahuasqui
# Archivo: main.py

# Importación de clases desde las carpetas correspondientes
from modelos import Soldador, SoldadorTIG
from servicios import ServicioTaller

def main():
    print("=== SISTEMA DE GESTIÓN DE SOLDADURA - MIGUEL CAHUASQUI ===\n")

    # 1. INSTANCIAS: Creación de objetos
    # Usamos tipos de datos correctos (str, int) como se pidió en el feedback
    soldador_basico = Soldador(nombre="Juan Pérez", id_empleado=101, especialidad="Arco Manual")
    soldador_experto = SoldadorTIG(nombre="Carlos Ruiz", id_empleado=102, certificacion_nivel=5)

    # 2. Uso del SERVICIO
    servicio = ServicioTaller()

    # 3. Demostración de HERENCIA y POLIMORFISMO
    # Ambos objetos ejecutan el mismo método, pero con distinto resultado
    servicio.asignar_trabajo(soldador_basico)
    print("") # Espacio
    servicio.asignar_trabajo(soldador_experto)

    print("\n--- Gestión de Horas y Encapsulamiento ---")
    
    # 4. Modificando atributos encapsulados a través de métodos
    soldador_basico.registrar_horas(8)
    soldador_experto.registrar_horas(6)

    # Calculando resultados
    print(servicio.calcular_pago_dia(soldador_basico, tarifa_hora=15.50))
    print(servicio.calcular_pago_dia(soldador_experto, tarifa_hora=25.00))

if __name__ == "__main__":
    main()