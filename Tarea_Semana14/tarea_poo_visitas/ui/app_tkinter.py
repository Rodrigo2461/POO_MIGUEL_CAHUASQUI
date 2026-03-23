# TS14 PROGRAMACION ORIENTADA A OBJETOS
# Realizado por: Miguel Cahuasqui
# Descripción: Capa de interfaz gráfica. Construye la ventana principal,
#              el formulario de entrada, los botones de acción y la tabla
#              de visualización. Se comunica con el servicio inyectado.

import tkinter as tk
from tkinter import ttk, messagebox

from servicios.visita_servicio import VisitaServicio


class AppTkinter:
    """
    Clase principal de la interfaz gráfica del sistema de visitantes.
    Recibe el servicio mediante inyección de dependencias para mantener
    la separación entre la capa de presentación y la lógica de negocio.
    """

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------
    def __init__(self, root: tk.Tk, servicio: VisitaServicio) -> None:
        """
        Inicializa la interfaz gráfica y sus componentes principales.

        Parámetros:
            root      (tk.Tk)         : Ventana raíz de Tkinter.
            servicio  (VisitaServicio): Servicio CRUD inyectado desde main.
        """
        # Referencia a la ventana raíz de Tkinter
        self.__root: tk.Tk = root

        # Servicio inyectado que gestiona la lógica de negocio
        self.__servicio: VisitaServicio = servicio

        # ── Configuración de la ventana principal ──────────────────────
        self.__root.title("Sistema de Registro de Visitantes")
        self.__root.geometry("780x520")
        self.__root.resizable(False, False)
        self.__root.configure(bg="#1e2a3a")

        # ── Construir secciones de la interfaz ─────────────────────────
        self.__construir_encabezado()   # Banner superior con título
        self.__construir_formulario()   # Campos de entrada de datos
        self.__construir_botones()      # Botones de acción CRUD
        self.__construir_tabla()        # Tabla (Treeview) de visitantes

    # ------------------------------------------------------------------
    # Sección: Encabezado
    # ------------------------------------------------------------------
    def __construir_encabezado(self) -> None:
        """
        Construye el banner superior que muestra el título del sistema
        y el nombre del autor del proyecto.
        """
        frame_header: tk.Frame = tk.Frame(
            self.__root, bg="#0f6cbd", pady=10
        )
        frame_header.pack(fill="x")

        tk.Label(
            frame_header,
            text="Sistema de Registro de Visitantes",
            font=("Courier New", 16, "bold"),
            fg="#ffffff",
            bg="#0f6cbd"
        ).pack()

        tk.Label(
            frame_header,
            text="TS14 · Programación Orientada a Objetos · Miguel Cahuasqui",
            font=("Courier New", 9),
            fg="#cce4f7",
            bg="#0f6cbd"
        ).pack()

    # ------------------------------------------------------------------
    # Sección: Formulario de entrada
    # ------------------------------------------------------------------
    def __construir_formulario(self) -> None:
        """
        Construye el panel con los campos de texto (Entry) donde el
        usuario ingresa los datos del visitante: cédula, nombre y motivo.
        Las variables de control (StringVar) permiten leer y limpiar
        los valores de forma programática.
        """
        frame_form: tk.LabelFrame = tk.LabelFrame(
            self.__root,
            text=" Datos del Visitante ",
            font=("Courier New", 10, "bold"),
            fg="#7ec8e3",
            bg="#1e2a3a",
            bd=2,
            relief="groove",
            padx=15,
            pady=10
        )
        frame_form.pack(fill="x", padx=20, pady=(12, 5))

        # ── Variables de control vinculadas a los campos Entry ─────────
        # Almacenan y permiten manipular el texto de cada campo
        self.__var_cedula: tk.StringVar = tk.StringVar()
        self.__var_nombre: tk.StringVar = tk.StringVar()
        self.__var_motivo: tk.StringVar = tk.StringVar()

        # Definición de los campos: (etiqueta, variable, fila, columna, ancho, columnspan)
        campos: list[tuple[str, tk.StringVar, int, int, int, int]] = [
            ("Cédula:",          self.__var_cedula, 0, 0, 15, 1),
            ("Nombre Completo:", self.__var_nombre, 0, 2, 30, 1),
            ("Motivo de Visita:", self.__var_motivo, 1, 0, 56, 3),
        ]

        # Creación dinámica de etiquetas y campos de texto
        for etiqueta, variable, fila, columna, ancho, col_span in campos:
            tk.Label(
                frame_form,
                text=etiqueta,
                font=("Courier New", 9, "bold"),
                fg="#adb5bd",
                bg="#1e2a3a"
            ).grid(row=fila, column=columna, sticky="w", padx=(10, 2), pady=5)

            tk.Entry(
                frame_form,
                textvariable=variable,
                font=("Courier New", 10),
                width=ancho,
                bg="#2c3e50",
                fg="#ecf0f1",
                insertbackground="#ecf0f1",
                relief="flat",
                bd=4
            ).grid(row=fila, column=columna + 1, columnspan=col_span, sticky="w", padx=(0, 15), pady=5)

    # ------------------------------------------------------------------
    # Sección: Botones de acción
    # ------------------------------------------------------------------
    def __construir_botones(self) -> None:
        """
        Construye el panel de botones que disparan las operaciones
        principales del sistema: Registrar, Eliminar y Limpiar Campos.
        Cada botón está conectado a su método manejador correspondiente.
        """
        frame_botones: tk.Frame = tk.Frame(self.__root, bg="#1e2a3a")
        frame_botones.pack(pady=8)

        # Configuración de botones: (texto, color de fondo, comando)
        botones: list[tuple[str, str, object]] = [
            ("Registrar",       "#27ae60", self.__accion_registrar),
            ("Eliminar",        "#e74c3c", self.__accion_eliminar),
            ("Limpiar Campos",  "#7f8c8d", self.__accion_limpiar),
        ]

        # Renderizar cada botón con estilo uniforme
        for texto, color, comando in botones:
            tk.Button(
                frame_botones,
                text=texto,
                command=comando,
                font=("Courier New", 10, "bold"),
                bg=color,
                fg="#ffffff",
                activebackground=color,
                activeforeground="#ffffff",
                relief="flat",
                padx=18,
                pady=7,
                cursor="hand2"
            ).pack(side="left", padx=10)

    # ------------------------------------------------------------------
    # Sección: Tabla de visualización
    # ------------------------------------------------------------------
    def __construir_tabla(self) -> None:
        """
        Construye el componente ttk.Treeview que muestra en tiempo real
        la lista de visitantes registrados. Incluye barra de desplazamiento
        vertical para manejar listas extensas.
        """
        frame_tabla: tk.LabelFrame = tk.LabelFrame(
            self.__root,
            text=" Visitantes Registrados ",
            font=("Courier New", 10, "bold"),
            fg="#7ec8e3",
            bg="#1e2a3a",
            bd=2,
            relief="groove",
            padx=10,
            pady=8
        )
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        # ── Estilo visual del Treeview ─────────────────────────────────
        style: ttk.Style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Custom.Treeview",
            background="#2c3e50",
            foreground="#ecf0f1",
            rowheight=26,
            fieldbackground="#2c3e50",
            font=("Courier New", 9)
        )
        style.configure(
            "Custom.Treeview.Heading",
            background="#0f6cbd",
            foreground="#ffffff",
            font=("Courier New", 10, "bold")
        )
        style.map("Custom.Treeview", background=[("selected", "#1a6fa8")])

        # ── Definición de columnas ─────────────────────────────────────
        columnas: tuple[str, ...] = ("cedula", "nombre", "motivo")

        self.__tabla: ttk.Treeview = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            style="Custom.Treeview"
        )

        # Encabezados y anchos de columna
        self.__tabla.heading("cedula", text="Cédula")
        self.__tabla.heading("nombre", text="Nombre Completo")
        self.__tabla.heading("motivo", text="Motivo de Visita")

        self.__tabla.column("cedula", width=140, anchor="center")
        self.__tabla.column("nombre", width=230, anchor="w")
        self.__tabla.column("motivo", width=330, anchor="w")

        # ── Barra de desplazamiento vertical ──────────────────────────
        scrollbar: ttk.Scrollbar = ttk.Scrollbar(
            frame_tabla,
            orient="vertical",
            command=self.__tabla.yview
        )
        self.__tabla.configure(yscrollcommand=scrollbar.set)

        self.__tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # ------------------------------------------------------------------
    # Acción: Registrar visitante
    # ------------------------------------------------------------------
    def __accion_registrar(self) -> None:
        """
        Maneja el evento del botón 'Registrar'.
        Lee los valores de los campos Entry, valida que no estén vacíos
        y delega la operación al servicio. Muestra mensajes de éxito
        o error mediante messagebox y refresca la tabla al finalizar.
        """
        # Leer y limpiar espacios en blanco de los campos
        cedula: str = self.__var_cedula.get().strip()
        nombre: str = self.__var_nombre.get().strip()
        motivo: str = self.__var_motivo.get().strip()

        # Validación: ningún campo puede estar vacío
        if not cedula or not nombre or not motivo:
            messagebox.showwarning(
                "Campos Incompletos",
                "Por favor, complete todos los campos antes de registrar."
            )
            return

        # Delegar la operación al servicio y obtener el resultado
        exito: bool
        mensaje: str
        exito, mensaje = self.__servicio.registrar(cedula, nombre, motivo)

        if exito:
            messagebox.showinfo("Registro Exitoso", mensaje)
            self.__accion_limpiar()     # Limpiar campos tras registro
            self.__actualizar_tabla()   # Refrescar la tabla
        else:
            messagebox.showerror("Error de Registro", mensaje)

    # ------------------------------------------------------------------
    # Acción: Eliminar visitante seleccionado
    # ------------------------------------------------------------------
    def __accion_eliminar(self) -> None:
        """
        Maneja el evento del botón 'Eliminar'.
        Verifica que el usuario haya seleccionado una fila en la tabla,
        extrae la cédula de esa fila y delega la eliminación al servicio.
        Solicita confirmación antes de proceder y refresca la tabla.
        """
        # Obtener la fila seleccionada en el Treeview
        seleccion: tuple = self.__tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin Selección",
                "Por favor, seleccione un visitante de la tabla para eliminarlo."
            )
            return

        # Extraer la cédula (primera columna) del registro seleccionado
        item: dict = self.__tabla.item(seleccion[0])
        cedula_seleccionada: str = item["values"][0]

        # Pedir confirmación al usuario antes de eliminar
        confirmar: bool = messagebox.askyesno(
            "Confirmar Eliminación",
            f"¿Está seguro de que desea eliminar al visitante con cédula '{cedula_seleccionada}'?"
        )

        if not confirmar:
            return

        # Delegar la eliminación al servicio
        exito: bool
        mensaje: str
        exito, mensaje = self.__servicio.eliminar(str(cedula_seleccionada))

        if exito:
            messagebox.showinfo("Eliminación Exitosa", mensaje)
            self.__actualizar_tabla()   # Refrescar la tabla
        else:
            messagebox.showerror("Error", mensaje)

    # ------------------------------------------------------------------
    # Acción: Limpiar campos del formulario
    # ------------------------------------------------------------------
    def __accion_limpiar(self) -> None:
        """
        Limpia el contenido de todos los campos Entry del formulario,
        dejándolos vacíos y listos para un nuevo ingreso de datos.
        """
        self.__var_cedula.set("")
        self.__var_nombre.set("")
        self.__var_motivo.set("")

    # ------------------------------------------------------------------
    # Método interno: Actualizar / refrescar la tabla
    # ------------------------------------------------------------------
    def __actualizar_tabla(self) -> None:
        """
        Borra todas las filas actuales del Treeview y las vuelve a
        insertar consultando la lista actualizada del servicio.
        Garantiza que la vista siempre refleje el estado real de los datos.
        """
        # Eliminar todas las filas existentes en el Treeview
        for fila in self.__tabla.get_children():
            self.__tabla.delete(fila)

        # Reinsertar los visitantes actuales provenientes del servicio
        from modelos.visitante import Visitante
        visitante: Visitante
        for visitante in self.__servicio.obtener_todos():
            self.__tabla.insert(
                "",
                "end",
                values=(visitante.cedula, visitante.nombre, visitante.motivo)
            )