animales = []

class Animal:
    # ENCAPSULAMIENTO:
    def __init__(self, nombre, edad):
        self.__nombre = nombre # Los guiones bajos indican que son privados.
        self.__edad = edad

    # Getters y Setters:
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    # ABSTRACCION:
    def hablar(self): # Método abstracto ya que se va a sobreescribir.
        pass

    def descripcion(self):
        return f'{self.__nombre} tiene {self.__edad} años'

# Herencia y Polimorfismo:
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza # Modo público

    def hablar(self):
        return 'Guau Guau'

    def descripcion(self):
        base = super().descripcion()
        return f'{base} - Es un perro de raza {self.raza}.'
    
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hablar(self):
        return 'Miau Miau'
    
    def descripcion(self):
        base = super().descripcion()
        return f'{base} - Es un gato de color {self.color}.'


# MENU:
def menu():
    while True:
        print("\n--- Menú de Animales ---")
        print("1. Registrar Perro")
        print("2. Registrar Gato")
        print("3. Ver todos los animales")
        print("4. Salir")

        opcion = input('Selecciona una opción: ')

        if opcion == '1':
            nombre = input('Nombre del perro: ')
            edad = input('Edad del perro: ')
            raza = input('Raza del perro: ')

            perro = Perro(nombre, edad, raza)
            animales.append(perro)
            print("Se ha guardado al perro correctamente. ")

        elif opcion == '2':
            nombre = input('Nombre del gato: ')
            edad = input('Edad del gato: ')
            color = input('Color del gato: ')

            gato = Gato(nombre, edad, color)
            animales.append(gato)
            print("Se ha guardado al gato correctamente. ")
        
        elif opcion == '3':
            if not animales:
                print('No se han guardado animales.')
            else:
                for i, animal in enumerate(animales, start=1):
                    print(f'\nAnimal #{i}')
                    print(animal.descripcion())
                    print('Hace: ', animal.hablar())
        elif opcion == '4':
            print('Saliendo del programa.')
            break

        else:
            print('Opción no válida.')

if __name__ == '__main__':
    print("EJEMPLO - CLASE 04/06")
    menu()