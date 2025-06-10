from .Nodo import Nodo

class listaCircular:
    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.primero == None:
            self.primero = nuevo
            self.primero.siguiente = self.primero
        else: 
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.primero

        self.size+=1
    
    def imprimir(self):
        actual = self.primero
        for elemento in range(self.size):
            print(actual.dato)
            actual = actual.siguiente
            elemento += 1

    def generarGrafico(self):
        graphvizTXT = "digraph listaCircular {\n"
        graphvizTXT += " splines=polyline;\n"
        graphvizTXT += " node [shape=box, style=filled];\n"

        # Crear nodos:
        actual = self.primero
        for i in range(self.size):
            graphvizTXT += f' node{i} [label=\"{actual.dato}\"]; \n'
            actual = actual.siguiente

        # conexiones:
        actual = self.primero
        for i in range(self.size - 1):
            graphvizTXT += f' node{i} -> node{i+1};\n'
        
        # conexion de ultimo a primero:
        graphvizTXT+= f' node{self.size - 1 } -> node0; \n'

        # rank same de todos los nodos:
        graphvizTXT += "  { rank = same; "
        for i in range(self.size):
            graphvizTXT += f"node{i}; "
        graphvizTXT += '}\n}'

        return graphvizTXT