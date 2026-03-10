# Realizado por: Miguel Cahuasqui
# Semana 13 - POO

import tkinter as tk
from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import AppGaraje

def main():
    """Punto de entrada de la aplicación."""
    # Instanciamos el servicio (lógica de negocio)
    servicio = GarajeServicio()
    
    # Creamos la ventana principal de Tkinter
    root = tk.Tk()
    
    # Instanciamos la interfaz gráfica pasándole la ventana y el servicio
    app = AppGaraje(root, servicio)
    
    # Iniciamos el bucle principal de eventos de la ventana
    root.mainloop()

if __name__ == "__main__":
    main()