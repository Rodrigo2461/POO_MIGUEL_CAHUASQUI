# =============================================================================
# TS14 PROGRAMACION ORIENTADA A OBJETOS
# Realizado por: Miguel Cahuasqui
# Descripción: Punto de entrada de la aplicación. Se encarga de instanciar
#              el servicio, inyectarlo en la interfaz gráfica y arrancar
#              el bucle principal de Tkinter.
# =============================================================================

import tkinter as tk

from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppTkinter


def main() -> None:
    """
    Función principal que orquesta el arranque de la aplicación.

    Pasos:
        1. Crear la ventana raíz de Tkinter.
        2. Instanciar el servicio CRUD (lógica de negocio).
        3. Inyectar el servicio en la interfaz gráfica (UI).
        4. Iniciar el bucle de eventos de Tkinter.
    """
    # Paso 1 – Crear la ventana raíz de Tkinter
    root: tk.Tk = tk.Tk()

    # Paso 2 – Instanciar el servicio que gestiona los visitantes
    servicio: VisitaServicio = VisitaServicio()

    # Paso 3 – Inyectar el servicio en la capa de interfaz gráfica
    # (Patrón de Inyección de Dependencias: la UI no crea su propio servicio)
    AppTkinter(root, servicio)

    # Paso 4 – Iniciar el bucle principal de eventos de la ventana
    root.mainloop()


# Punto de entrada estándar de Python
if __name__ == "__main__":
    main()