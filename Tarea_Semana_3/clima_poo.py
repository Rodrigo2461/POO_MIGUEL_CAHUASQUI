# HECHO POR MIGUEL CAHUASQUI
# Práctica: Programación Orientada a Objetos - Promedio Semanal del Clima

# --------------------------------------------------------------------------------
# CLASE: ClimaSemanal
# --------------------------------------------------------------------------------
class ClimaSemanal:
    """
    Representa la información de las temperaturas mínimas y máximas de una semana.
    Encapsula los datos y los métodos para manipularlos (ingreso y cálculo).
    """

    # Constructor de la clase: Inicializa los atributos (datos)
    def __init__(self):
        # Atributos privados (convención con _) para fomentar el encapsulamiento
        self._temperaturas_minimas = []
        self._temperaturas_maximas = []
        self._dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # ----------------------------------------------------------------------------
    # MÉTODO DE ENTRADA DE DATOS
    # ----------------------------------------------------------------------------
    def ingresar_temperaturas(self):
        """
        Método para solicitar al usuario las temperaturas mínimas y máximas.
        Los datos se almacenan directamente en los atributos de la instancia.
        """
        print("\n--- INGRESO DE DATOS DEL CLIMA ---")
        
        # Llenar temperaturas mínimas
        self._temperaturas_minimas = self._solicitar_temperaturas("Mínima")
        
        # Llenar temperaturas máximas
        self._temperaturas_maximas = self._solicitar_temperaturas("Máxima")
        
        print("\n--- INGRESO DE DATOS COMPLETADO ---")

    # Método auxiliar privado (solo se usa dentro de la clase)
    def _solicitar_temperaturas(self, tipo_temp):
        """ Lógica para solicitar 7 temperaturas para un tipo específico. """
        print(f"\n> Ingrese las temperaturas {tipo_temp.upper()}:")
        temps = []
        for dia in self._dias_semana:
            while True:
                try:
                    # Se solicita la temperatura para cada día
                    temp = float(input(f"  {tipo_temp} del {dia}: "))
                    temps.append(temp)
                    break
                except ValueError:
                    print("  Error: Ingrese un número válido para la temperatura.")
        return temps

    # ----------------------------------------------------------------------------
    # MÉTODOS DE CÁLCULO
    # ----------------------------------------------------------------------------
    def calcular_promedio_minimo(self):
        """ Calcula el promedio semanal de las temperaturas mínimas. """
        return self._calcular_promedio(self._temperaturas_minimas)

    def calcular_promedio_maximo(self):
        """ Calcula el promedio semanal de las temperaturas máximas. """
        return self._calcular_promedio(self._temperaturas_maximas)

    # Método auxiliar privado (para la lógica de cálculo que es similar)
    def _calcular_promedio(self, lista_temperaturas):
        """ Lógica reutilizable para calcular el promedio de una lista. """
        if not lista_temperaturas:
            return 0.0
        return sum(lista_temperaturas) / len(lista_temperaturas)

    # ----------------------------------------------------------------------------
    # MÉTODO DE PRESENTACIÓN DE RESULTADOS
    # ----------------------------------------------------------------------------
    def mostrar_resultados(self):
        """ Muestra las temperaturas ingresadas y los promedios calculados. """
        # Los cálculos se hacen justo antes de mostrar la información
        promedio_minimo = self.calcular_promedio_minimo()
        promedio_maximo = self.calcular_promedio_maximo()
        
        print("\n=========================================================")
        print("                   RESULTADOS POO")
        print("=========================================================")
        # Acceso a los atributos internos de la clase
        print(f"Temperaturas Mínimas Ingresadas: {self._temperaturas_minimas}")
        print(f"Temperaturas Máximas Ingresadas: {self._temperaturas_maximas}")
        print("---------------------------------------------------------")
        # Se redondea el resultado a dos decimales para una mejor presentación
        print(f"PROMEDIO SEMANAL DE TEMPERATURAS MÍNIMAS: {promedio_minimo:.2f}°C")
        print(f"PROMEDIO SEMANAL DE TEMPERATURAS MÁXIMAS: {promedio_maximo:.2f}°C")
        print("=========================================================")


# --------------------------------------------------------------------------------
# LÓGICA PRINCIPAL (Uso de la Clase)
# --------------------------------------------------------------------------------
def main_poo():
    """
    Función principal que crea y utiliza la instancia (objeto) de la clase ClimaSemanal.
    """
    print("=========================================================")
    print("     INICIO PROGRAMA POO - PROMEDIO CLIMA SEMANAL")
    print("=========================================================")
    
    # 1. Crear una instancia (objeto) de la clase ClimaSemanal
    reporte_clima = ClimaSemanal()
    
    # 2. Usar el método de la instancia para ingresar los datos
    reporte_clima.ingresar_temperaturas()
    
    # 3. Usar el método de la instancia para mostrar los resultados (que incluye el cálculo)
    reporte_clima.mostrar_resultados()


# Ejecutar la función principal 
if __name__ == "__main__":
    main_poo()

