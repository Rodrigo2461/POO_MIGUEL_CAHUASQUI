Comparación de Paradigmas: Promedio Semanal del Clima (Tradicional vs. POO)

Este repositorio contiene dos implementaciones en Python para calcular el promedio de las temperaturas mínimas y máximas de una semana, demostrando la aplicación práctica de la Programación Estructurada y la Programación Orientada a Objetos (POO).

Código Tradicional 
Paradigma: Programación Estructurada/Tradicional (Basada en Funciones). Descripción: La lógica se maneja con funciones independientes. Los datos (listas de temperaturas) son variables externas que se generan en una función y luego se pasan explícitamente a otra función (calcular_promedio_semanal) para su procesamiento.

Código Orientado a Objetos 

Paradigma: Programación Orientada a Objetos (POO). Descripción: Utiliza la Clase ClimaSemanal para encapsular los datos (_temperaturas_minimas, _temperaturas_maximas) y los métodos (calcular_promedio_minimo) dentro de una única entidad. El objeto reporte_clima es responsable de manejar su propia información y cálculos.

Ventajas Clave de la POO en este Caso

El enfoque POO es ideal porque:

Encapsulamiento: Los datos de las temperaturas están protegidos dentro de la Clase ClimaSemanal, haciendo más fácil la gestión de la información semanal como una unidad lógica.

Modularidad: La lógica de la aplicación principal (main_poo) es muy simple, ya que simplemente crea el objeto y llama a sus métodos, aislando la complejidad del procesamiento dentro de la clase.

Claridad del Código: El modelo de la Clase ClimaSemanal es una representación directa y clara de la entidad que se está estudiando.