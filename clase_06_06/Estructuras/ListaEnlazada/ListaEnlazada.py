from .Nodo import Nodo


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.size = 0
    
    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.primero == None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.size += 1 

    def imprimir(self):
        actual = self.primero
        while actual.siguiente != None:
            print('         ' ,  actual.dato)
            actual = actual.siguiente
        print('         ' , actual.dato)

    def imprimirObjeto(self):
        actual = self.primero
        while actual.siguiente != None:
            print(actual.dato.nombre)
            actual = actual.siguiente
        print(actual.dato.nombre)

    def imprimirConSegundaLista(self):
        actual = self.primero
        while actual.siguiente != None:
            print(" > " + actual.dato.nombre)
            actual.dato.listado.imprimir()
            actual = actual.siguiente
        print(" > " + actual.dato.nombre)
        actual.dato.listado.imprimir()