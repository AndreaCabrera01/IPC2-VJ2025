from .NodoInterno import NodoInterno
from .ListaEncabezado import ListaEncabezado
from .NodoCabecera import NodoCabecera

class MatrizDispersa():
    def __init__(self, capa):
        self.capa = 0
        self.filas = ListaEncabezado('fila')
        self.columnas = ListaEncabezado('columa')

    def insertar(self, valor, fila, columna):
        nuevo = NodoInterno(fila, columna, valor)

        nodoFila, nodoColumna = self.revisarCabeceras(fila, columna)


        # Insertar nodo Interno en la fila Correspondiente:
        if nodoFila.acceso is None:
            nodoFila.acceso = nuevo
        else: # Si ya está apuntanto a un nodo, debemos insertarlo ORDENADAMENTE

            # Si el nuevo nodo es menor (altura) que el acceso actual.
            if nuevo.y < nodoFila.acceso.y:
                nuevo.siguiente = nodoFila.acceso
                nodoFila.acceso.anterior = nuevo
                nodoFila.acceso = nuevo
            else: # SI no se cumple, se busca de lado a lado en dónde se inserta:
                actual = nodoFila.acceso
                while actual is not None:
                    if nuevo.y < actual.y:
                        nuevo.siguiente = actual
                        nuevo.anterior = actual.anterior
                        actual.anterior.siguiente = nuevo
                        actual.anterior = nuevo
                        break
                    elif nuevo.x == actual.x and nuevo.y == actual.y: #LO MISMO
                        return
                    else:
                        if actual.siguiente is None:
                            actual.siguiente = nuevo
                            nuevo.anterior = actual
                            break
                        else:
                            actual = actual.siguiente

        # Insertamos el nodo en la columna correspondiente:
        if nodoColumna.acceso is None:
            nodoColumna.acceso = nuevo
        else:  # Si ya está apuntando a un nodo, debemos insertarlo ordenadamente.
            # Si el nuevo nodo es menor que el acceso actual:
            if nuevo.x < nodoColumna.acceso.x:
                nuevo.abajo = nodoColumna.acceso
                nodoColumna.acceso.arriba = nuevo
                nodoColumna.acceso = nuevo
            else:  # Si no se cumple, se busca de arriba hacia abajo para buscar dónde
                # insertarlo.
                actual = nodoColumna.acceso
                while actual is not None:
                    if nuevo.x < actual.x:
                        nuevo.abajo = actual
                        nuevo.arriba = actual.arriba
                        actual.arriba.abajo = nuevo
                        actual.arriba = nuevo
                        break
                    elif nuevo.x == actual.x and nuevo.y == actual.y:
                        return  # Si el nodo ya existe, no lo insertamos.
                    else:
                        if actual.abajo is None:
                            actual.abajo = nuevo
                            nuevo.arriba = actual
                            break
                        else:
                            actual = actual.abajo  

    def revisarCabeceras(self, fila, columna):
        # Revisar si las cabeceras de fila y columna existen, si no, las crea.

        nodoFila = self.filas.getEncabezado(fila)
        nodoColumna = self.columnas.getEncabezado(columna)


        if nodoFila is None:
            nodoFila = NodoCabecera(fila)
            self.filas.insertarNodoCabecera(nodoFila)

        if nodoColumna is None:
            nodoColumna = NodoCabecera(columna)
            self.columnas.insertarNodoCabecera(nodoColumna)

        return nodoFila, nodoColumna