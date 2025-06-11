from .Nodo import Nodo
class Pila:
    def __init__(self):
        self.first = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.first
        self.first = nuevo
        self.size += 1

    def extraer(self):
        if self.first is None:
            return None
        temp = self.first
        self.first = self.first.siguiente
        self.size -= 1
        return temp.dato
    
    def ver_cima(self):
        return self.first.dato if self.first else None
    
    def esta_vacia(self):
        return self.first is None
    
    def imprimir(self):
        temp = self.first
        while temp is not None:
            print(temp.dato)
            temp = temp.siguiente
    
    def graphviz(self):
        graph = "digraph Pila {\n node [shape=record]; \n"
        temp = self.first
        i = 0
        while temp is not None:
            graph += f'nodo{i} [label="{{ {temp.dato} }}"];\n'
            if temp.siguiente is not None:
                graph += f'nodo{i} -> nodo{i+1};\n'
            temp = temp.siguiente
            i += 1
        graph += "}"
        return graph