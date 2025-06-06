from Estructuras.ListaEnlazada.ListaEnlazada import ListaEnlazada

class Persona:
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad
        self.listado = ListaEnlazada()


    def __str__(self):
        return f' nombre: {self.nombre} | carnet: {self.carnet} | edad: {self.edad}'