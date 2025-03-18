class Animal:
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
class Gato(Animal):
    
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def maullar(self):
        print("¡Miau!")
        
gato1 = Gato("Wilson",4)

gato1.maullar()

print("Luis Augusto Procel Amendaño")
         
        