# Realizado por: Miguel Cahuasqui
# Semana 13 - POO

import tkinter as tk
from tkinter import ttk, messagebox
from modelos.vehiculo import Vehiculo
from servicios.garaje_servicio import GarajeServicio

class AppGaraje:
    """Clase que maneja toda la Interfaz Gráfica de Usuario (GUI)."""
    
    def __init__(self, root: tk.Tk, servicio: GarajeServicio):
        self.root = root
        self.servicio = servicio
        
        # Configuración principal de la ventana
        self.root.title("Sistema de Gestión de Garaje - Miguel Cahuasqui")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        self._crear_widgets()

    def _crear_widgets(self):
        """Crea y posiciona los elementos visuales en la ventana."""
        # --- Marco del Formulario ---
        frame_form = tk.LabelFrame(self.root, text="Registro de Vehículo", padx=10, pady=10)
        frame_form.pack(padx=10, pady=10, fill="x")

        # Etiquetas y Campos de texto
        tk.Label(frame_form, text="Placa:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_placa = tk.Entry(frame_form)
        self.entry_placa.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Marca:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_marca = tk.Entry(frame_form)
        self.entry_marca.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Propietario:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_propietario = tk.Entry(frame_form)
        self.entry_propietario.grid(row=2, column=1, pady=5, padx=5)

        # Botones
        frame_botones = tk.Frame(frame_form)
        frame_botones.grid(row=3, column=0, columnspan=2, pady=10)

        btn_agregar = tk.Button(frame_botones, text="Agregar Vehículo", command=self.evento_agregar, bg="#4CAF50", fg="white")
        btn_agregar.pack(side="left", padx=5)

        btn_limpiar = tk.Button(frame_botones, text="Limpiar Campos", command=self.evento_limpiar, bg="#f47836", fg="white")
        btn_limpiar.pack(side="left", padx=5)

        # --- Marco de la Tabla ---
        frame_tabla = tk.LabelFrame(self.root, text="Vehículos Registrados", padx=10, pady=10)
        frame_tabla.pack(padx=10, pady=5, fill="both", expand=True)

        # Tabla (Treeview)
        columnas = ("placa", "marca", "propietario")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        self.tabla.heading("placa", text="Placa")
        self.tabla.heading("marca", text="Marca")
        self.tabla.heading("propietario", text="Propietario")
        
        # Tamaños de columnas
        self.tabla.column("placa", width=100)
        self.tabla.column("marca", width=120)
        self.tabla.column("propietario", width=200)
        
        self.tabla.pack(fill="both", expand=True)

    def evento_agregar(self):
        """Captura los datos de los entries, valida y guarda en el servicio."""
        placa = self.entry_placa.get().strip()
        marca = self.entry_marca.get().strip()
        propietario = self.entry_propietario.get().strip()

        # Validación de campos vacíos
        if not placa or not marca or not propietario:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        # Creación del objeto y guardado
        nuevo_vehiculo = Vehiculo(placa, marca, propietario)
        exito = self.servicio.agregar_vehiculo(nuevo_vehiculo)

        if exito:
            messagebox.showinfo("Éxito", "Vehículo registrado correctamente.")
            self.actualizar_tabla()
            self.evento_limpiar()
        else:
            messagebox.showerror("Error", "Ya existe un vehículo con esa placa.")

    def evento_limpiar(self):
        """Borra el texto de todos los campos de entrada."""
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)
        # Regresa el cursor al primer campo
        self.entry_placa.focus()

    def actualizar_tabla(self):
        """Limpia la tabla visual y la vuelve a llenar con los datos del servicio."""
        # Borrar filas actuales
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        
        # Insertar datos actualizados
        vehiculos = self.servicio.obtener_vehiculos()
        for v in vehiculos:
            self.tabla.insert("", tk.END, values=(v.placa, v.marca, v.propietario))