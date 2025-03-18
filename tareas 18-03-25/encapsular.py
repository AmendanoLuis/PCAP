class Persona:
    contador_personas = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad
        Persona.contador_personas += 1

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La edad no puede ser negativa")
        self.__edad = cantidad

    @classmethod
    def cantidad_personas(cls):
        return f"Se han creado {cls.contador_personas} personas."

    @staticmethod
    def saludo_general():
        print("¡Hola desde la clase Persona!")

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}"


e1 = Empleado("Luis", 22, "Programador")
print(e1)

e2 = Empleado("Ana", 30, "Diseñadora")
print(e2)

print(Persona.cantidad_personas())

Persona.saludo_general()  

print("Luis Augusto Procel Amendaño")