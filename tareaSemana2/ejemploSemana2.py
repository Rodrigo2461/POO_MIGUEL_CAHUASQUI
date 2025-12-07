# ============================================
#     Clase base: Vehiculo
# ============================================

# --------------------------------------------
# 1. ABSTRACCIÓN (Aplicada en la clase Vehiculo)
# --------------------------------------------
# La abstracción se usa para representar únicamente lo esencial
# de un vehículo. En este ejemplo, la clase Vehiculo incluye solo
# los atributos básicos que definen a cualquier vehículo:
# marca, modelo, color y año.
#
# La abstracción permite que esta clase sirva como modelo general
# para otras clases más específicas (como Auto o Motocicleta),
# ocultando detalles innecesarios y enfocándose en lo importante.
# --------------------------------------------

class Vehiculo:
    def __init__(self, marca, modelo, color, anio):
        # =====================================================
        # 2. ENCAPSULAMIENTO (Protección de los datos)
        # -----------------------------------------------------
        # Los atributos están protegidos usando un guion bajo,
        # lo que indica que no deben ser modificados directamente.
        #
        # Además, se utilizan métodos getters y setters para
        # controlar el acceso a estos datos. Esto permite:
        # Validar valores antes de asignarlos
        # Proteger la integridad de la información
        # Evitar cambios directos no controlados
        #
        # =====================================================
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._anio = anio

    # -------- MÉTODO DE ABSTRACCIÓN --------
    def mostrar_info(self):
        return f"{self._marca} {self._modelo} ({self._color}), año {self._anio}"

    # -------- MÉTODOS DE ENCAPSULAMIENTO --------
    def get_marca(self):
        return self._marca

    def set_marca(self, nueva_marca):
        if len(nueva_marca) > 1:
            self._marca = nueva_marca

    def get_anio(self):
        return self._anio

    def set_anio(self, nuevo_anio):
        if nuevo_anio > 1900:
            self._anio = nuevo_anio


# ============================================
#     HERENCIA: Auto y Motocicleta
# ============================================

# ---------------------------------------------------------
# 3. HERENCIA (Auto y Motocicleta heredan de Vehiculo)
# ---------------------------------------------------------
# La herencia permite crear nuevas clases basadas en una clase
# existente. En este ejemplo:
#
# • Auto(Vehiculo)
# • Motocicleta(Vehiculo)
#
# Gracias a la herencia:
# Se reutilizan los atributos marca, modelo, color, año
# No es necesario reescribir código repetido
# Se agregan atributos propios: num_puertas y cilindrada
# Se puede expandir comportamiento sin duplicar código
# ---------------------------------------------------------

class Auto(Vehiculo):
    def __init__(self, marca, modelo, color, anio, num_puertas):
        # Llama al constructor de Vehiculo
        super().__init__(marca, modelo, color, anio)
        self.num_puertas = num_puertas

    # ---------------------------------------------
    # 4. POLIMORFISMO: método mostrar_info() redefinido
    # ---------------------------------------------
    # El polimorfismo permite que el mismo método (mostrar_info)
    # funcione diferente según el tipo de objeto.
    #
    # Aquí, Auto redefine mostrar_info() para incluir sus puertas.
    # ---------------------------------------------
    def mostrar_info(self):
        return (f"Auto: {self._marca} {self._modelo} ({self._color}), "
                f"año {self._anio} - Puertas: {self.num_puertas}")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, color, anio, cilindrada):
        super().__init__(marca, modelo, color, anio)
        self.cilindrada = cilindrada

    # Polimorfismo nuevamente aplicado
    def mostrar_info(self):
        return (f"Motocicleta: {self._marca} {self._modelo} ({self._color}), "
                f"año {self._anio} - Cilindrada: {self.cilindrada}cc")


# ============================================
#     PROGRAMA PRINCIPAL (uso de las clases)
# ============================================

# Creando dos instancias de Vehiculo
v1 = Vehiculo("Ford", "Ranger", "Blanco", 2020)
v2 = Vehiculo("Chevrolet", "D-Max", "Negro", 2019)

# Creando dos instancias de Auto
a1 = Auto("Toyota", "Corolla", "Rojo", 2022, 4)
a2 = Auto("Mazda", "CX-5", "Azul", 2023, 5)

# Creando dos instancias de Motocicleta
m1 = Motocicleta("Yamaha", "YZF-R15", "Azul", 2021, 150)
m2 = Motocicleta("Honda", "CBR500R", "Rojo", 2022, 500)

# Mostrando información de vehículos
print(v1.mostrar_info())
print(v2.mostrar_info())

# Mostrando información de autos (ejemplo de polimorfismo)
print(a1.mostrar_info())
print(a2.mostrar_info())

# Mostrando información de motocicletas (ejemplo de polimorfismo)
print(m1.mostrar_info())
print(m2.mostrar_info())

print("\n--- Usando encapsulación (modificando datos de forma controlada) ---")
# Usando encapsulación (modificando datos de forma controlada)
v1.set_marca("Ford Ranger")
v1.set_anio(2021)
print(v1.mostrar_info())

a1.set_marca("Toyota Yaris")
a1.set_anio(2023)
print(a1.mostrar_info())