#Creación de la superclase "Animal"
class Animal:
  #Definir el método "sonido"
  def sonido(self):
    pass

#Creación de la subclase 1, junto con su método y atributo
class Perro(Animal):
  #Se asigna ell mismo método de la superclase "Animal"
  def sonido (self):
    return "Guau"

#Creación de la subclase 2, junto con su método y atributo
class Gato(Animal):
  #Se asigna el mismo método de la superclase "Animal"
  def sonido (self):
    return "Miau"

# Creación de la función "Hacer sonido"
 def hacer_sonido(animal: Animal):
  print(animal.sonido())

#Creación de los objetos 
perro=Perro()
gato=Gato()

#Salida de los objetos 
hacer_sonido(perro)
hacer_sonido(gato)
