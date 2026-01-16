# Proyecto Semana 4 - UNIVERSIDAD ESTATAL AMAZONICA
#  Programación Orientada a Objetos (POO)
# Contexto del mundo real:
#  Taller mecánico de autos
# Autor: MIGUEL CAHUASQUI
# Fecha: 21 de diciembre de 2025

# En este ejemplo se modela un TALLER MECÁNICO sencillo usando POO.
# Se representan:
# - Vehículos
# - Clientes
# - Órdenes de servicio (reparaciones)
# - El TallerMecanico que administra todo


class Cliente:
    """
    Representa a un cliente del taller mecánico.
    Atributos: nombre y teléfono.
    """
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_info(self):
        """Muestra los datos básicos del cliente."""
        print(f"Cliente: {self.nombre} - Tel: {self.telefono}")


class Vehiculo:
    """
    Representa un vehículo que llega al taller.
    Atributos: placa, marca y modelo, y el cliente dueño.
    """
    def __init__(self, placa, marca, modelo, dueno):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.dueno = dueno  # objeto Cliente

    def mostrar_info(self):
        """Muestra información del vehículo y su dueño."""
        print(f"Vehículo: {self.placa} - {self.marca} {self.modelo}")
        print(f"Dueño: {self.dueno.nombre}")


class OrdenServicio:
    """
    Representa una orden de servicio en el taller.
    Atributos:
    - vehiculo: objeto Vehiculo
    - descripcion: trabajo a realizar
    - costo_estimado: valor aproximado del servicio
    - estado: abierta o finalizada
    """
    def __init__(self, vehiculo, descripcion, costo_estimado):
        self.vehiculo = vehiculo
        self.descripcion = descripcion
        self.costo_estimado = costo_estimado
        self.estado = "abierta"

    def cerrar_orden(self):
        """Marca la orden como finalizada."""
        self.estado = "finalizada"

    def mostrar_detalle(self):
        """Muestra el detalle completo de la orden de servicio."""
        print("===================================")
        print(f"Orden para el vehículo: {self.vehiculo.placa}")
        print(f"Cliente: {self.vehiculo.dueno.nombre}")
        print(f"Trabajo a realizar: {self.descripcion}")
        print(f"Costo estimado: ${self.costo_estimado:.2f}")
        print(f"Estado: {self.estado}")
        print("===================================\n")


class TallerMecanico:
    """
    Clase principal que representa el taller mecánico.
    Administra:
    - Lista de vehículos registrados
    - Órdenes de servicio
    - Total facturado (suma de costos estimados de órdenes finalizadas)
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []       # lista de Vehiculo
        self.ordenes = []         # lista de OrdenServicio
        self.total_facturado = 0  # dinero acumulado

    def registrar_vehiculo(self, vehiculo):
        """Registra un vehículo en el taller."""
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        """Muestra todos los vehículos registrados en el taller."""
        print(f"\nVehículos registrados en el taller '{self.nombre}':")
        if not self.vehiculos:
            print("No hay vehículos registrados.\n")
            return
        for i, v in enumerate(self.vehiculos, start=1):
            print(f"{i}. {v.placa} - {v.marca} {v.modelo} (Dueño: {v.dueno.nombre})")
        print()

    def crear_orden_servicio(self, vehiculo, descripcion, costo_estimado):
        """
        Crea una nueva orden de servicio para un vehículo.
        Devuelve el objeto OrdenServicio creado.
        """
        orden = OrdenServicio(vehiculo, descripcion, costo_estimado)
        self.ordenes.append(orden)
        return orden

    def finalizar_orden(self, orden):
        """
        Finaliza una orden y suma su costo al total facturado.
        """
        if orden.estado == "finalizada":
            print("Esta orden ya está finalizada.\n")
            return
        orden.cerrar_orden()
        self.total_facturado += orden.costo_estimado
        print("La orden ha sido marcada como finalizada.\n")

    def mostrar_resumen_ordenes(self):
        """Muestra cuántas órdenes hay y cuánto se ha facturado."""
        total_ordenes = len(self.ordenes)
        print(f"Resumen de órdenes del taller '{self.nombre}':")
        print(f"Órdenes creadas: {total_ordenes}")
        print(f"Total facturado: ${self.total_facturado:.2f}\n")


# ---------------------------------------------------------
# BLOQUE PRINCIPAL: simulación simple del taller mecánico
# ---------------------------------------------------------

# 1. Crear el taller
taller = TallerMecanico("Taller Mecánico MIGUEL")

# 2. Crear algunos clientes
cliente1 = Cliente("Carlos", "0991234567")
cliente2 = Cliente("Elena", "0987654321")

# 3. Crear vehículos y registrarlos en el taller
auto1 = Vehiculo("ABC-123", "Toyota", "Corolla", cliente1)
auto2 = Vehiculo("XYZ-789", "Chevrolet", "Spark", cliente2)

taller.registrar_vehiculo(auto1)
taller.registrar_vehiculo(auto2)

# 4. Mostrar vehículos registrados
taller.mostrar_vehiculos()

# 5. Crear órdenes de servicio
orden1 = taller.crear_orden_servicio(auto1, "Cambio de aceite y filtros", 45.00)
orden2 = taller.crear_orden_servicio(auto2, "Revisión de frenos", 60.00)

# 6. Mostrar detalle de cada orden
orden1.mostrar_detalle()
orden2.mostrar_detalle()

# 7. Finalizar una de las órdenes
taller.finalizar_orden(orden1)

# 8. Volver a mostrar la orden para ver el cambio
orden1.mostrar_detalle()

# 9. Mostrar resumen general de órdenes y total facturado
taller.mostrar_resumen_ordenes()
