# Archivo: main.py
# Programa principal que demuestra el uso de POO

# Importamos las clases que vamos a usar
from modelos.soldadura import SoldaduraMIG, SoldaduraTIG
from modelos.soldador import Soldador
from servicios.gestion import GestionSoldadura

# Funcion principal del programa
def main():
    print("===========================================")
    print("  SISTEMA DE GESTION DE SOLDADURA")
    print("  Proyecto de Programacion Orientada a Objetos")
    print("===========================================\n")
    
    # Creamos un objeto de la clase GestionSoldadura
    sistema = GestionSoldadura()
    
    # ============================================
    # PARTE 1: CREAR SOLDADORES
    # ============================================
    print("\n--- PARTE 1: CREANDO SOLDADORES ---")
    print("Demostracion de ENCAPSULACION con atributos privados\n")
    
    # Creamos objetos de tipo Soldador
    soldador1 = Soldador("Juan Perez", "1234567890", 5)
    soldador2 = Soldador("Maria Lopez", "0987654321", 3)
    
    # Agregamos los soldadores al sistema
    sistema.agregar_soldador(soldador1)
    sistema.agregar_soldador(soldador2)
    
    # Demostracion de encapsulacion: no podemos acceder directamente a la cedula
    print("\nDemostracion de ENCAPSULACION:")
    print("Cedula protegida de " + soldador1.nombre + ": " + soldador1.obtener_cedula())
    print("No se puede acceder a soldador1.__cedula directamente")
    
    # ============================================
    # PARTE 2: CREAR PROCESOS DE SOLDADURA
    # ============================================
    print("\n\n--- PARTE 2: CREANDO PROCESOS DE SOLDADURA ---")
    print("Demostracion de HERENCIA: MIG y TIG heredan de Soldadura\n")
    
    # Creamos un objeto de SoldaduraMIG (hereda de Soldadura)
    # HERENCIA: SoldaduraMIG tiene todos los metodos de la clase Soldadura
    proceso_mig = SoldaduraMIG(amperaje=150, voltaje=25, gas="Argon")
    sistema.agregar_proceso(proceso_mig)
    
    # Creamos un objeto de SoldaduraTIG (hereda de Soldadura)
    # HERENCIA: SoldaduraTIG tambien hereda de Soldadura
    proceso_tig = SoldaduraTIG(amperaje=120, voltaje=20, electrodo="Tungsteno")
    sistema.agregar_proceso(proceso_tig)
    
    print("Ambas clases heredan de la clase base Soldadura")
    print("Heredan metodos como calcular_potencia() y obtener_amperaje()")
    
    # ============================================
    # PARTE 3: DEMOSTRAR POLIMORFISMO
    # ============================================
    print("\n\n--- PARTE 3: DEMOSTRACION DE POLIMORFISMO ---")
    print("El metodo iniciar() funciona diferente en MIG y TIG\n")
    
    # Ejecutamos el metodo iniciar() en el proceso MIG
    print("Ejecutando proceso MIG:")
    sistema.ejecutar_proceso(0)
    
    # Ejecutamos el metodo iniciar() en el proceso TIG
    print("Ejecutando proceso TIG:")
    sistema.ejecutar_proceso(1)
    
    print("POLIMORFISMO: Mismo metodo (iniciar), diferente comportamiento")
    
    # ============================================
    # PARTE 4: USO DE METODOS HEREDADOS
    # ============================================
    print("\n\n--- PARTE 4: USO DE METODOS HEREDADOS ---")
    print("Ambos procesos pueden usar calcular_potencia() heredado\n")
    
    # Comparamos las potencias de ambos procesos
    sistema.comparar_potencias()
    
    # ============================================
    # PARTE 5: MODIFICAR ATRIBUTOS PRIVADOS
    # ============================================
    print("\n\n--- PARTE 5: MODIFICACION SEGURA DE DATOS ---")
    print("Demostracion de ENCAPSULACION con validacion\n")
    
    # Intentamos establecer un amperaje invalido (negativo)
    print("Intentando establecer amperaje negativo:")
    proceso_mig.establecer_amperaje(-50)
    
    # Establecemos un amperaje valido
    print("\nEstableciendo amperaje valido:")
    proceso_mig.establecer_amperaje(180)
    print("Nuevo amperaje: " + str(proceso_mig.obtener_amperaje()) + " A")
    
    # ============================================
    # PARTE 6: REGISTRAR TRABAJOS
    # ============================================
    print("\n\n--- PARTE 6: REGISTRO DE TRABAJOS ---\n")
    
    # Registramos trabajos completados
    soldador1.registrar_trabajo()
    soldador1.registrar_trabajo()
    soldador2.registrar_trabajo()
    
    # ============================================
    # PARTE 7: MOSTRAR INFORMACION FINAL
    # ============================================
    print("\n\n--- PARTE 7: INFORMACION FINAL ---")
    
    # Mostramos todos los soldadores
    sistema.mostrar_soldadores()
    
    # Mostramos todos los procesos
    sistema.mostrar_procesos()
    
    # ============================================
    # RESUMEN DE CONCEPTOS POO
    # ============================================
    print("\n===========================================")
    print("  RESUMEN DE CONCEPTOS DE POO APLICADOS")
    print("===========================================")
    print("\n1. HERENCIA:")
    print("   - Clase base: Soldadura")
    print("   - Clases derivadas: SoldaduraMIG, SoldaduraTIG")
    print("   - Uso de super() para llamar al constructor padre")
    
    print("\n2. ENCAPSULACION:")
    print("   - Atributos privados: __amperaje, __voltaje, __cedula")
    print("   - Metodos getter y setter para acceso controlado")
    print("   - Validacion de datos antes de modificarlos")
    
    print("\n3. POLIMORFISMO:")
    print("   - Metodo iniciar() sobrescrito en cada clase")
    print("   - Mismo metodo, comportamiento diferente")
    
    print("\n===========================================")
    print("  FIN DEL PROGRAMA")
    print("===========================================\n")


# Punto de entrada del programa
# Esta linea verifica que el archivo se ejecute directamente
if __name__ == "__main__":
    main()