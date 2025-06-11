class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    
    def __str__(self):
        return (self.dato)