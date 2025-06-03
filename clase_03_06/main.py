def funcDummy():
    print("Hola desde la función")

def sumaFunc(num1, num2):
    return num1 + num2

def restaFunc(num1, num2):
    return num1 - num2

def divisionFunc(num1, num2):
    return num1 / num2

def multiplicacionFunc(num1, num2):
    return num1 * num2

def Menu():
    print('¿Qué operación quieres hacer?')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. Division')
    print('5. Salir')

    opcion = input()
    return opcion


if __name__ == '__main__':
    print('Hola, estoy en el main')

    # Este es un comentario de 1 línea.
    
    '''
    Hola
    Esto es 
        un
    comentario
        multilínea
    '''

    # VARIABLES:
    string = 'cadena de texto'
    StringLargo = '''
        Soy
    un string
    largo
    '''

    a = -1 #entero
    b = 3

    c = 1.0 # flotante
    d = 2.0

    # complejo
    complejo1 = 1 + 2j # complejos siempre van a llevar una 'j' al final.
    complejo2 = 3 + 4j

    print(StringLargo)

    e = "Dobles"
    f = 'simples'

    # Booleans:
    g = True
    h = False

    #tipo NONE:
    i = None # NoneType, representa la ausencia de valor.

    # ¿Queremos saber el tipo que posee actualmente una variable?
    # type()

    print(type(a)) # <class 'int'>
    print(type(c)) # <class 'float'>
    print(type(complejo1)) 
    print(type(e)) 
    print(type(g)) 
    print(type(i)) 


    # Operaciones:
    # + , -, *, /

    suma = a + b
    resta = a - b
    multiplicacion = a*b
    division= a/b

    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)

    print('Ingrese su nombre: ')
    nombre = input()

    edad = input('Ingrese su edad: ')

    # print('Hola, ' + nombre + ' su edad es de:', int(edad))
    # print(f'Hola, mi nombre es {nombre}, tengo {edad} años')
    # Condicionales:
    # IF:

    if a == 1:
        print("Si, la variable 'a' tiene el valor de 1.")
    else:
        print('No, la variable "a" no posee el valor de 1.')
        
    # operadores lógicos:
    # Python: and, or, not ------------ Java: &&, ||, !

    if a == 1 and b == 2:
        print('Se cumple')
    elif a == 2 or int(edad) == 23:
        print("Se cumple alguna de las condiciones")
    elif not a == 1:
        print('Se cumple de "a" NO es 1.')
    else:
        print('Nada se cumple')

    # Match-case:
    option = 1
    match option:
        case 1:
            print('1')
        case 2:
            print('2')
        case _:
            print('opcion no valida')

    # operadores de comparacion:
    # ==, !=, <, >, <=, >=
    # igual que, no es igual, menor qué, mayor qué, menor igual que, mayor igual qué

    if int(edad) >= 18:
        print('Mayor de edad')
    else: 
        print('Menor de edad')

    # CICLOS:
    # FOR:

    for i in range (1, 11):
        print(i, "HOLA")

    for i in range(0,10,2):
        print(i)

    '''
    for(int i=0; i<10; i+=2){
        ...
    }
    '''

    # WHILE:
    print("Contador con While:")
    contador = 0
    while contador < 10:
        print(contador)
        contador +=2

    # FUNCIONES:
    funcDummy()
    print('SUMA: ', sumaFunc(22,22))
    resta = restaFunc(9, 5)
    print('RESTA', resta)
    print('MULTIPLICACION: ', multiplicacionFunc(2,6))
    print('DIVISION: ', divisionFunc(49,7))

    print('Tipo de lo que devuelve la funcion: ', type(divisionFunc(49,7)))

    # saltos de linea:
    print()
    print('prueba')

    # Listas:
    listaEjemplo = [1,2,3]
    listaEjemplo2 = [1, 'A', False]

    for elemento in listaEjemplo:
        print(elemento)

    for elemento in listaEjemplo2:
        print(elemento)

    for i in range(0, len(listaEjemplo)):
        print(listaEjemplo[i])

    # opcionSeleccionada = Menu()
    # while opcionSeleccionada != '5':
    #     num1 = int(input('Ingrese un número: '))
    #     num2 = int(input('Ingrese el segundo número: '))

    #     if opcionSeleccionada == '1':
    #         print('La suma de los números es: ' + str(sumaFunc(num1, num2)))
    #     if opcionSeleccionada == '2':
    #         print('La resta de los números es: ' + str(restaFunc(num1, num2)))
    #     if opcionSeleccionada == '3':
    #         print('La multiplicacion de los números es: ' + str(multiplicacionFunc(num1, num2)))
    #     if opcionSeleccionada == '4':
    #         print('La división de los números es: ' + str(divisionFunc(num1, num2)))

    #     opcionSeleccionada = Menu()
    # print('Gracias por usar nuestra calculadora.')


    # Realizando el Menú por medio del Match-Case:
    opcionSeleccionada = Menu()
    while opcionSeleccionada != '5':
        num1 = int(input('Ingrese un número: '))
        num2 = int(input('Ingrese el segundo número: '))

        match opcionSeleccionada:
            case '1':
                print('La suma de los números es: ' + str(sumaFunc(num1, num2)))
            case '2':
                print('La resta de los números es: ' + str(restaFunc(num1, num2)))
            case '3':
                print('La multiplicacion de los números es: ' + str(multiplicacionFunc(num1, num2)))
            case '4':
                print('La división de los números es: ' + str(divisionFunc(num1, num2)))
        opcionSeleccionada = Menu()
    print('Gracias por usar nuestra calculadora.')