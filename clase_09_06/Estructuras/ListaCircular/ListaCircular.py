from .Nodo import Nodo

class ListaCircular:
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

        self.size += 1

    def shuffle_right(self, movimientos):
        if self.primero is None or self.size == 0 or movimientos == 0:
            return
        
        movimientos = movimientos % self.size
        if movimientos == 0:
            return
        
        # Encontrar el nuevo primero (size - movimientos):
        nuevo_primero = self.primero
        for _ in range(self.size - movimientos):
            nuevo_primero = nuevo_primero.siguiente
        
        self.primero = nuevo_primero

    def imprimir(self):
        actual = self.primero
        for elemento in range(self.size):
            print(actual.dato)
            actual = actual.siguiente
            elemento+=1

    def generarGrafico(self):
        graphvizTXT = '''digraph ReporteMazo {\n
    splines=ortho;
    node [shape=box; style=filled];
    subgraph cluster_mazo {
    label=\"Lista Circular - Mazo\"
    bgcolor=gray;
'''

        # Crear nodos:
        actual = self.primero
        for i in range(self.size):
            graphvizTXT += f'node{i} [label=\"{actual.dato.valor}\", fillcolor=\"{actual.dato.color}\"];\n'
            actual = actual.siguiente

        # conexiones:
        for i in range(self.size - 1):
            graphvizTXT += f'node{i} -> node{i+1} [color=black];\n'
        
        # conexion circular:
        if self.size > 1:
            graphvizTXT+= f'node{self.size-1} -> node0;\n'

        # Nodos con el mismo rango:
        graphvizTXT += "{rank=same; "
        for i in range(self.size):
            graphvizTXT += f'node{i}; '
        graphvizTXT+="}\n"
        
        graphvizTXT += "}\n}"

        return graphvizTXT