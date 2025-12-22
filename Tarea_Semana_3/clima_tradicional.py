# HECHO POR MIGUEL CAHUASQUI
# Práctica: Programación Tradicional - Promedio Semanal del Clima

# --------------------------------------------------------------------------------
# PASO 1: FUNCIÓN PARA LA ENTRADA DE DATOS (TEMPERATURAS)
# --------------------------------------------------------------------------------
def obtener_temperaturas_semanales(tipo_temp):
    """
    Solicita al usuario ingresar las temperaturas diarias para un tipo específico.
    
    Args:
        tipo_temp (str): Etiqueta para el tipo de temperatura (ej: 'Mínima' o 'Máxima').
    
    Returns:
        list: Lista de 7 floats que representan las temperaturas diarias.
    """
    print(f"\n--- INGRESO DE TEMPERATURAS {tipo_temp.upper()} ---")
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    for dia in dias:
        while True:
            try:
                # Se solicita la temperatura para cada día de la semana
                temp = float(input(f"Ingrese la temperatura {tipo_temp} del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                # Manejo de error si la entrada no es un número válido
                print("Error: Por favor, ingrese un número válido.")
    
    return temperaturas

# --------------------------------------------------------------------------------
# PASO 2: FUNCIÓN PARA EL CÁLCULO DEL PROMEDIO
# --------------------------------------------------------------------------------
def calcular_promedio_semanal(lista_temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    
    Args:
        lista_temperaturas (list): Lista de números (temperaturas).
    
    Returns:
        float: El promedio de las temperaturas.
    """
    if not lista_temperaturas:
        # Evita la división por cero si la lista está vacía
        return 0.0
        
    # Suma todos los elementos y divide por el número total de elementos
    suma_total = sum(lista_temperaturas)
    promedio = suma_total / len(lista_temperaturas)
    return promedio

# --------------------------------------------------------------------------------
# PASO 3: FUNCIÓN PRINCIPAL (LÓGICA DEL PROGRAMA)
# --------------------------------------------------------------------------------
def main_tradicional():
    """
    Función principal que orquesta la lógica del programa en el enfoque tradicional.
    """
    print("=========================================================")
    print("  INICIO PROGRAMA TRADICIONAL - PROMEDIO CLIMA SEMANAL")
    print("=========================================================")
    
    # 1. Obtener los datos usando las funciones de entrada de datos
    temps_minimas = obtener_temperaturas_semanales("Mínima")
    temps_maximas = obtener_temperaturas_semanales("Máxima")
    
    # 2. Calcular los promedios usando la función de cálculo
    promedio_minimo = calcular_promedio_semanal(temps_minimas)
    promedio_maximo = calcular_promedio_semanal(temps_maximas)
    
    # 3. Mostrar los resultados
    print("\n=========================================================")
    print("                 RESULTADOS TRADICIONALES")
    print("=========================================================")
    print(f"Temperaturas Mínimas Ingresadas: {temps_minimas}")
    print(f"Temperaturas Máximas Ingresadas: {temps_maximas}")
    print("---------------------------------------------------------")
    # Se redondea el resultado a dos decimales para una mejor presentación
    print(f"PROMEDIO SEMANAL DE TEMPERATURAS MÍNIMAS: {promedio_minimo:.2f}°C")
    print(f"PROMEDIO SEMANAL DE TEMPERATURAS MÁXIMAS: {promedio_maximo:.2f}°C")
    print("=========================================================")


# Ejecutar la función principal 
if __name__ == "__main__":
    main_tradicional()

