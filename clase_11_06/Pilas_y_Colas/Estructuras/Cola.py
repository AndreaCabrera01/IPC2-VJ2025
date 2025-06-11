from .Nodo import Nodo

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.ultimo is None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.size += 1

    def extraer(self):
        if self.primero is None:
            return None
        temp = self.primero
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        self.size -= 1
        return temp.dato

    def imprimir(self):
        temp = self.primero
        while temp is not None:
            print(temp.dato)
            temp = temp.siguiente

    def esta_vacia(self):
        return self.primero is None

    def ver_primero(self):
        return self.primero.dato if self.primero else None

    def graphviz(self):
        graph = "digraph Cola {\n rankdir=LR; node [shape=record]; \n"
        temp = self.primero

        i = 0
        while temp is not None:
            graph += f'nodo{i} [label="{{ {temp.dato} }}"];\n'
            if temp.siguiente is not None:
                graph += f'nodo{i} -> nodo{i+1};\n'
            temp = temp.siguiente
            i += 1
        graph += "}"
        return graph