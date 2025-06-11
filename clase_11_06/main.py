import re

if __name__ == '__main__':
    # Ficheros:
    # Apertura de ficheros:

    archivo = open('fichero.txt', 'w')
    archivo.write('Me llamo Andrea y mi carnet es 1111')
    archivo.close()

    archivo = open('fichero.txt', 'r')
    contenido = archivo.read()
    print(contenido)
    archivo.close()

    # Modo Add:
    archivo = open('fichero.txt', 'a')
    archivo.write('\nHola clase de IPC2')
    archivo.close()

    # With para abrir y cerrar ficheros:
    with open('fichero.txt', 'w') as openedFile:
        openedFile.write('Desde with')

    # manejo de excepciones:
    try:
        with open('ficheroNOexistente.txt', 'r') as archivoNoExistente:
            contenido = archivoNoExistente.read()
            print(contenido)
    except FileNotFoundError:
        print("El fichero que quiere abrir no existe. ")
    except Exception as e:
        print('Error inesperado: ', e)


    # Tuplas:
    tupla = (1,2,3,4,5)
    print(tupla)
    print(tupla[0])
    print(tupla[1:3])
    print(tupla[1:])
    print(tupla[:3])
    print(tupla[-1])

    # Diccionario:
    diccionario = {'nombre': 'Juan', 'edad':25, 'cursos': ['Python', 'Java', 'Javascript']}
    print(diccionario)
    print(diccionario['edad'])

    # Regex:
    texto = 'En esta cadena se encuentra una palabra mágica'
    patron = "mágica"

    print(re.search(patron, texto))

    # coincidencia de dígitos:
    txt = "Yo tengo 23 años."
    x = re.findall('\d', txt)
    print(x)

    # coincidencia de letras:
    txt = "La lluvia en Sevilla es una maravilla"
    x = re.findall('a', txt)
    print(x)