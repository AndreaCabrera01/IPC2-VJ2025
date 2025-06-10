from Persona import Persona
from Estructuras.ListaEnlazada.ListaEnlazada import ListaEnlazada
from Estructuras.ListaDEnlazada.ListaDEnlazada import ListaDEnlazada
from Estructuras.ListaCircular.ListaCircular import listaCircular
from Estructuras.ListaDCircular.ListaDCircular import ListaDCircular
from os import system
if __name__ == '__main__':
    print('LISTA ENLAZADA ----------')
    lista1 = ListaEnlazada()
    # lista1.insertar(1)
    # lista1.insertar(6)
    # lista1.insertar(3)
    # persona = Persona('ANDREA', 2020, 23)
    # persona.listado.insertar(1)
    # persona.listado.insertar(2)
    # persona.listado.insertar(3)
    # persona.listado.insertar(4)


    # persona2 = Persona('ANDREA', 2020, 23)
    # persona2.listado.insertar(1)
    # persona2.listado.insertar(2)
    # persona2.listado.insertar(3)
    # persona2.listado.insertar(4)


    # lista1.insertar(persona)
    # lista1.insertar(persona2)
    # lista1.insertar(Persona('ANDREA', 2020, 23))
    # lista1.insertar(Persona('MARIA', 2020, 23))
    # lista1.insertar(Persona('CABRERA', 2020, 23))

    lista1.insertar(1)
    lista1.insertar(2)
    lista1.insertar(3)

    grafo1 = lista1.generarGrafico()
    with open("grafo_lista_enlazada.dot", "w") as file:
        file.write(grafo1)
    system('dot -Tpdf grafo_lista_enlazada.dot -o ReporteLE.pdf')

    print('LISTA DOBLEMENTE ENLAZADA ----------')
    lista2 = ListaDEnlazada()
    lista2.insertar('Andrea')
    lista2.insertar('María')
    lista2.insertar('Cabrera')

    lista2.imprimir()
    lista2.imprimirReversa()

    grafo2 = lista2.generarGrafico()
    with open("grafo_lista_denlazada.dot", "w") as file:
        file.write(grafo2)
    system('dot -Tpdf grafo_lista_denlazada.dot -o ReporteLDE.pdf')


    print('LISTA CIRCULAR SIMPLEMENTE ENLAZADA -----------')
    lista3 = listaCircular()
    lista3.insertar('A')
    lista3.insertar('B')
    lista3.insertar('C')

    lista3.imprimir()

    grafo3 = lista3.generarGrafico()
    with open("grafo_lista_cenlazada.dot", "w") as file:
        file.write(grafo3)
    system('dot -Tpdf grafo_lista_cenlazada.dot -o ReporteLC.pdf')


    print('LISTA CIRCULAR DOBLEMENTE ENLAZADA ----------')
    lista4 = ListaDCircular()

    lista4.insertar('1')
    lista4.insertar('2')
    lista4.insertar('3')
    lista4.insertar('xd')

    lista4.imprimir()

    grafo4 = lista4.generarGrafico()
    with open("grafo_lista_cdenlazada.dot", "w") as file:
        file.write(grafo4)
    system('dot -Tpdf grafo_lista_cdenlazada.dot -o ReporteLCD.pdf')