# elementTree:
import xml.etree.ElementTree as ET
from os import system
from Objetos.Carta import Carta
from Estructuras.ListaCircular.ListaCircular import ListaCircular

mazo = ListaCircular()

def generar_reporte():
    reporte = mazo.generarGrafico()
    with open("grafo_mazo.dot", "w") as file:
        file.write(reporte)

    system('dot -Tpdf grafo_mazo.dot -o Reporte_graphviz.pdf')
    print('Reporte Generado: Reporte_graphviz.pdf')

def mover_posicion(movimientos):
    mazo.shuffle_right(movimientos=movimientos)
    print(f'Lista Movida {movimientos} posiciones')

def leer_archivo(archivo):
    try:
        tree = ET.parse(archivo)
        root = tree.getroot()

        contador = 0
        cartas = root.find('mazo_disponible/cartas')

        for carta in cartas.findall('carta'):
            if contador < 51:
                color = carta.attrib.get('color')
                valor = carta.text.strip()
                carta_obj = Carta(color, valor)
                
                contador += 1
                mazo.insertar(carta_obj)
            else:
                print("Maximo de cartas alcanzado (51)")
                break

        return True
    except FileNotFoundError:
        print(f"Archivo no encontrado: {archivo}")
        return None
        
    except ET.ParseError as e:
        print(f"Error al procesar el archivo XML: {e}")
        return None