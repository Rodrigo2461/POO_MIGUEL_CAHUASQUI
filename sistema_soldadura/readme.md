Las Clases
Soldadura (Clase Base)
Representa un proceso de soldadura generico.

Atributos privados: amperaje y voltaje
Metodos: calcular potencia, iniciar proceso

SoldaduraMIG y SoldaduraTIG (Clases Derivadas)
Heredan de Soldadura, cada una con sus caracteristicas especificas.

MIG: usa gas protector
TIG: usa electrodo de tungsteno

Soldador
Representa un trabajador.

Atributos privados: cedula y experiencia
Metodos: registrar trabajos, mostrar informacion

GestionSoldadura
Administra todo el sistema.

Guarda listas de soldadores y procesos
Ejecuta operaciones del sistema

Conceptos POO Aplicados
HERENCIA

Soldadura es la clase padre
SoldaduraMIG y SoldaduraTIG son clases hijas
Las hijas heredan metodos como calcular_potencia()

ENCAPSULACION

Atributos privados: __amperaje, __voltaje, __cedula
Se acceden con metodos getter y setter
Los setters validan que los datos sean correctos

POLIMORFISMO

El metodo iniciar() existe en todas las clases
Cada clase lo hace diferente
MIG muestra info del gas, TIG muestra info del electrodo