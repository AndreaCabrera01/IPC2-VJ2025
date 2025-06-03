# EJERCICIO 1:
'''
Escribe un programa que pida al usuario su nombre y edad, luego muestre un mensaje con los datos proporcionados.
'''
print('Hola, ingresa tu nombre y tu edad.')
nombre = input('Nombre: ')
edad = input('Edad: ')

print('Hola, ' + nombre + ' tu edad es de: ', edad)

# EJERCICIO 2:
'''
Escribe un programa que pida un número al usuario y diga si es par o impar.
'''
input_numero = input('Ingresa un número: ')
numero = int(input_numero)
if numero % 2 == 0:
    print('El número ', numero, ' es par.')
else:
    print('El número ', numero, ' es impar.')


# EJERCICIO 3:
'''
Escribe un programa que imprima los números del 1 al 10, uno por línea.
'''

for i in range(1, 11):
    print(i)
