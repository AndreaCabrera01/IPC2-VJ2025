from Estructuras.Cola import Cola
from Estructuras.Pila import Pila

class Farmacia:
    def __init__(self):
        self.recetas_pendientes = Cola()
        self.recetas_atendidas = Pila()

    def recibir_receta(self, receta):
        print(f'Recibida: {receta}')
        self.recetas_pendientes.insertar(receta)

    def atender_receta(self):
        if self.recetas_pendientes.esta_vacia():
            print('No hay recetas pendientes por atender.')
            return
        receta = self.recetas_pendientes.extraer()
        print(f'Atendiendo receta: {receta}')
        self.recetas_atendidas.insertar(receta)

    def ver_ultima_atendida(self):
        cima = self.recetas_atendidas.ver_cima()
        print("Última receta atendida:", cima if cima else "Ninguna")

    def mostrar_pendientes(self):
        print('RECETAS PENDIENTES:')
        if self.recetas_pendientes.esta_vacia():
            print('Ninguna receta pendiente.')
        else:
            self.recetas_pendientes.imprimir()

    def mostrar_historial(self):
        print("Historial de las recetas atendidas: ")
        if self.recetas_atendidas.esta_vacia():
            print("No hay nada en el historial")
        else:
            self.recetas_atendidas.imprimir()

    def verGraficoPendientes(self):
        print("Generando el gráfico....")
        return self.recetas_pendientes.graphviz()

    def verGraficoAtendidas(self):
        print("Generando el gráfico....")
        return self.recetas_atendidas.graphviz()