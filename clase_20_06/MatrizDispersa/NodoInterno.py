class NodoInterno():
    def __init__(self, x, y, valor):
        self.x = x # Coordenada en x (fila)
        self.y = y # Coordenada en y (columna)
        self.valor = valor # valor del nodo interno
        # apuntadores:
        self.siguiente = None
        self.anterior = None
        self.abajo = None
        self.arriba = None