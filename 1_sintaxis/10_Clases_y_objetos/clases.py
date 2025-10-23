"""
Una clase es una plantilla o plano que define:

-Caracteristicas (atributos): color, precio, raza, altura
- Comportramientos(métodos): arrancar, ladrar, iniciar
"""

class Coche:
    # definimos atributos y métodos
    pass

mi_coche = Coche()
coche_de_amigo = Coche()

class Libro: 
    # atributos: titulo, autor, numero de paginas
    # metodos: abrir, leer, cerrar, subrayar
    def __init__(self, titulo, autor, numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas

libro_python = Libro()

"""
Constructor: método especial que se ejecuta
automáticamente cuando creamos un objeto

El método __init__ se ejecuta automáticamente al crear el objeto
y sirve para dejar el objeto con datos iniciales
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
persona1 = Persona("Carlos",50)
