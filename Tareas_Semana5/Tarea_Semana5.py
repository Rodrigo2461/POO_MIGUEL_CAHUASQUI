
"""
Sistema de Cálculo de Dilatación Térmica
Funcionalidad: Calcula cómo varía el área de materiales cuando se calientan
o enfrían, aplicando conceptos de dilatación térmica superficial.
HECHO POR MIGUEL CAHUASQUI
(Semana 05) Tarea: Tipos de datos, Identificadores
"""


class Material:
    """
    Clase que representa un material y calcula su dilatación térmica.
    
    Atributos:
    -----------
    nombre : str
        Nombre del material
    coeficiente_dilatacion : float
        Coeficiente de dilatación lineal del material (1/°C)
    """
    
    def __init__(self, nombre, coeficiente_dilatacion):
        """
        Constructor de la clase Material.
        
        Parámetros:
        -----------
        nombre : str
            Nombre del material
        coeficiente_dilatacion : float
            Coeficiente de dilatación lineal (×10⁻⁶ /°C)
        """
        self.nombre = nombre
        self.coeficiente = coeficiente_dilatacion
    
    def calcular_area_final(self, area_inicial, temperatura_inicial, temperatura_final):
        """
        Calcula el área final después de la dilatación térmica.
        
        Fórmula: A_final = A_inicial × (1 + 2α × ΔT)
        
        Parámetros:
        -----------
        area_inicial : float
            Área inicial del material (m²)
        temperatura_inicial : float
            Temperatura inicial (°C)
        temperatura_final : float
            Temperatura final (°C)
        
        Retorna:
        --------
        float: Área final después de la dilatación
        """
        # Calcular el cambio de temperatura
        delta_temperatura = temperatura_final - temperatura_inicial
        
        # Calcular el área final (dilatación superficial)
        # Coeficiente superficial β = 2α
        area_final = area_inicial * (1 + 2 * self.coeficiente * delta_temperatura)
        
        return area_final
    
    def calcular_variacion_area(self, area_inicial, area_final):
        """
        Calcula la variación del área.
        
        Parámetros:
        -----------
        area_inicial : float
            Área inicial
        area_final : float
            Área final
        
        Retorna:
        --------
        float: Variación del área
        """
        return area_final - area_inicial
    
    def mostrar_resultado(self, area_inicial, temperatura_inicial, temperatura_final):
        """
        Calcula y muestra los resultados de la dilatación térmica.
        
        Parámetros:
        -----------
        area_inicial : float
            Área inicial del material
        temperatura_inicial : float
            Temperatura inicial
        temperatura_final : float
            Temperatura final
        """
        # Calcular área final
        area_final = self.calcular_area_final(area_inicial, temperatura_inicial, temperatura_final)
        
        # Calcular variación
        variacion = self.calcular_variacion_area(area_inicial, area_final)
        
        # Determinar si se dilató o contrajo (boolean)
        se_dilato = variacion > 0
        
        # Mostrar resultados
        print("\n" + "=" * 60)
        print("RESULTADOS DE LA DILATACIÓN TÉRMICA")
        print("=" * 60)
        print(f"Material: {self.nombre}")
        print(f"Coeficiente de dilatación: {self.coeficiente} ×10⁻⁶ /°C")
        print(f"\nÁrea inicial: {area_inicial:.4f} m²")
        print(f"Temperatura inicial: {temperatura_inicial}°C")
        print(f"Temperatura final: {temperatura_final}°C")
        print(f"Cambio de temperatura: {temperatura_final - temperatura_inicial}°C")
        print(f"\nÁrea final: {area_final:.4f} m²")
        print(f"Variación del área: {variacion:.6f} m²")
        
        if se_dilato:
            print(f"\n El material se DILATÓ (aumentó su área)")
        else:
            print(f"\n El material se CONTRAJO (disminuyó su área)")
      


# Programa principal
def main():
    """
    Función principal que ejecuta el programa de dilatación térmica.
    """
    print("=" * 60)
    print("CALCULADORA DE DILATACIÓN TÉRMICA")
    print("=" * 60)
    
    # Diccionario con materiales comunes y sus coeficientes (×10⁻⁶ /°C)
    materiales_disponibles = {
        "1": ("Aluminio", 23.0),
        "2": ("Acero", 11.0),
        "3": ("Cobre", 17.0),
        "4": ("Vidrio", 9.0),
        "5": ("Concreto", 12.0)
    }
    
    # Mostrar menú de materiales
    print("\nSeleccione un material:")
    print("1. Aluminio")
    print("2. Acero")
    print("3. Cobre")
    print("4. Vidrio")
    print("5. Concreto")
    
    # Tipo string - Opción del usuario
    opcion = input("\nIngrese el número del material: ")
    
    # Validar opción
    if opcion in materiales_disponibles:
        nombre_material, coef = materiales_disponibles[opcion]
        
        # Crear objeto de la clase Material
        material = Material(nombre_material, coef * 1e-6)
        
        print(f"\n Material seleccionado: {nombre_material}")
        
        # Solicitar datos al usuario
        # Tipo float - Área inicial
        area_inicial = float(input("\nIngrese el área inicial del material (m²): "))
        
        # Tipo float - Temperatura inicial
        temp_inicial = float(input("Ingrese la temperatura inicial (°C): "))
        
        # Tipo float - Temperatura final
        temp_final = float(input("Ingrese la temperatura final (°C): "))
        
        # Calcular y mostrar resultados usando el objeto
        material.mostrar_resultado(area_inicial, temp_inicial, temp_final)
        
    else:
        print("\n Opción inválida. Por favor, ejecute el programa nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()