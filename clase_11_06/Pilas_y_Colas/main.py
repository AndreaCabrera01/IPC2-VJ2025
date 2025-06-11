from Farmacia import Farmacia

from os import system

farmacia = Farmacia()

# Ingresar Recetas:
farmacia.recibir_receta("Receta de Andrea")
farmacia.recibir_receta("Receta de Ale")
farmacia.recibir_receta("Receta de Luna")
farmacia.recibir_receta("Receta de Kiara")
farmacia.recibir_receta("Receta de Pablo")
farmacia.recibir_receta("Receta de Pedro")

# mostrar pendientes:
farmacia.mostrar_pendientes()
with open('pendientes.dot', 'w') as file:
    file.write(farmacia.verGraficoPendientes())

system(f'dot -Tpdf pendientes.dot -o pendientes.pdf')

# atender la receta:
farmacia.atender_receta()
farmacia.atender_receta()
farmacia.atender_receta()

# ver la última receta atendida:
farmacia.ver_ultima_atendida()

# historial de recetas atendidas:
farmacia.mostrar_historial()
with open('atendidas.dot', 'w') as file:
    file.write(farmacia.verGraficoAtendidas())

system(f'dot -Tpdf atendidas.dot -o atendidas.pdf')