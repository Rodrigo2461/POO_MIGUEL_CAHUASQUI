from servicios.servicio_soldador import ServicioSoldador
from modelos.soldador_mig import SoldadorMIG
from modelos.soldador_tig import SoldadorTIG

servicio = ServicioSoldador()

def menu():
    while True:
        print("\n=== DASHBOARD SOLDADORES ===")
        print("1 Registrar Soldador MIG")
        print("2 Registrar Soldador TIG")
        print("3 Ver Soldadores")
        print("0 Salir")

        op = input("Opcion: ")

        if op == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            exp = float(input("Experiencia: "))
            gas = input("Tipo Gas: ")

            s = SoldadorMIG(nombre, edad, exp, gas)
            servicio.agregar(s)

        elif op == "2":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            exp = float(input("Experiencia: "))
            material = input("Material: ")

            s = SoldadorTIG(nombre, edad, exp, material)
            servicio.agregar(s)

        elif op == "3":
            servicio.mostrar()

        elif op == "0":
            break
