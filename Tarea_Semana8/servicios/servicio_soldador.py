class ServicioSoldador:

    def __init__(self):
        self.lista = []

    def agregar(self, soldador):
        self.lista.append(soldador)

    def mostrar(self):
        for s in self.lista:
            print("-------------------")
            print("Nombre:", s.get_nombre())
            print("Edad:", s.get_edad())
            print("Experiencia:", s.get_experiencia())
            print("Trabajo:", s.tipo_trabajo())  # POLIMORFISMO
