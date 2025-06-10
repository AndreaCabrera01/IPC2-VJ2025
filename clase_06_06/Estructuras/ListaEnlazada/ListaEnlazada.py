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

    def generarGrafico(self):
        graphvizTXT = "digraph listaEnlazada {\n"
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

        # rank same de todos los nodos:
        graphvizTXT += "  { rank = same; "
        for i in range(self.size):
            graphvizTXT += f"node{i} "
        graphvizTXT += '}\n}'

        return graphvizTXT