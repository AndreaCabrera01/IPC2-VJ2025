from .Nodo import Nodo

class ListaDCircular():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
            # Actualizamos los punteros:
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            nuevo.siguiente = self.primero

            self.primero.anterior = nuevo
            self.ultimo = nuevo
        self.size += 1

    def imprimir(self):
        actual = self.primero

        for i in range(self.size):
            print(actual.dato)
            actual = actual.siguiente
            i += 1

    def generarGrafico(self):
        graphvizTXT = "digraph listaDCEnlazada {\n"
        graphvizTXT += " splines=polyline;\n"
        graphvizTXT += " node [shape=box, style=filled];\n"
        graphvizTXT += " edge [dir=both];\n"

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
        graphvizTXT += f' node{self.size - 1 } -> node0; \n'
        print("PRUEBA DE GENERACIÓN: ", f' node{self.size - 1 } -> node0;')
        # rank same de todos los nodos:
        graphvizTXT += "  { rank = same; "
        for i in range(self.size):
            graphvizTXT += f"node{i} "
        graphvizTXT += '}\n}'

        return graphvizTXT