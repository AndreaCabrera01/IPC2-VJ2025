from .NodoCabecera import NodoCabecera

class ListaEncabezado(): # Lista doblemente Enlazada.
    def __init__(self, tipo):
        self.primero = None
        self.ultimo = None

        self.tipo = tipo

        self.size = 0

    def insertarNodoCabecera(self, nuevo):
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            # ORDENADAMENTE (depende el ID):
            # Si el nuevo nodo es menor que el primero:
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            # Si el nodo nuevo es mayor que el último:
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            # Recorremos hasta encontrar la posición correcta
            else: 
                actual = self.primero 
                while actual is not None:
                    if nuevo.id < actual.id:
                        nuevo.siguiente = actual
                        nuevo.anterior = actual.anterior
                        actual.anterior.siguiente = nuevo
                        actual.anterior =  nuevo
                        break
                    elif nuevo.id > actual.id:
                        actual = actual.siguiente
                    else:
                        # EL ID YA EXISTE, NO SE HACE NADA
                        return
        self.size += 1

    def getEncabezado(self, id) -> NodoCabecera:
        # BUSCAR UN NODO DE CABECERA POR SU ID:
        actual = self.primero
        while actual is not None:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None