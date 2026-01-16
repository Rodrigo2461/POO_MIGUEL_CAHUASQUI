# Archivo: servicios/gestion.py
# Contiene la logica para gestionar soldadores y procesos

# Importamos las clases que vamos a usar
from modelos.soldadura import Soldadura
from modelos.soldador import Soldador

class GestionSoldadura:
    
    # Constructor: inicializa las listas vacias
    def __init__(self):
        # Lista para guardar los soldadores
        self.soldadores = []
        # Lista para guardar los procesos de soldadura
        self.procesos = []
    
    # Metodo para agregar un soldador a la lista
    def agregar_soldador(self, soldador):
        self.soldadores.append(soldador)
        print("Soldador " + soldador.nombre + " agregado correctamente")
    
    # Metodo para agregar un proceso de soldadura a la lista
    def agregar_proceso(self, proceso):
        self.procesos.append(proceso)
        print("Proceso de soldadura " + proceso.tipo + " agregado correctamente")
    
    # Metodo para ejecutar un proceso
    # POLIMORFISMO: el metodo iniciar() se comporta diferente segun el tipo de soldadura
    def ejecutar_proceso(self, indice):
        # Verificamos que el indice sea valido
        if indice >= 0 and indice < len(self.procesos):
            proceso = self.procesos[indice]
            print("\n--- Ejecutando Proceso ---")
            # Llamamos al metodo iniciar, que funciona diferente en MIG y TIG
            print(proceso.iniciar())
            print("--------------------------\n")
        else:
            print("Error: Indice no valido")
    
    # Metodo para mostrar todos los soldadores
    def mostrar_soldadores(self):
        if len(self.soldadores) == 0:
            print("No hay soldadores registrados")
        else:
            print("\n--- Lista de Soldadores ---")
            # Recorremos la lista con un ciclo for
            for i in range(len(self.soldadores)):
                print("\nSoldador " + str(i) + ":")
                self.soldadores[i].mostrar_info()
            print("---------------------------\n")
    
    # Metodo para mostrar todos los procesos
    def mostrar_procesos(self):
        if len(self.procesos) == 0:
            print("No hay procesos registrados")
        else:
            print("\n--- Lista de Procesos ---")
            # Recorremos la lista de procesos
            for i in range(len(self.procesos)):
                print("\nProceso " + str(i) + ":")
                print(self.procesos[i].mostrar_info())
            print("-------------------------\n")
    
    # Metodo para comparar potencias de los procesos
    def comparar_potencias(self):
        if len(self.procesos) == 0:
            print("No hay procesos para comparar")
        else:
            print("\n--- Comparacion de Potencias ---")
            # Recorremos todos los procesos
            for proceso in self.procesos:
                potencia = proceso.calcular_potencia()
                print(proceso.tipo + ": " + str(potencia) + " W")
            print("--------------------------------\n")