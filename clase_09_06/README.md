# Comandos:

## Entorno virtual:

En ciertos casos, es recomendable crear un entorno virtual para evitar conflictos entre dependencias de diferentes proyectos. Para crear un entorno virtual, puedes usar `venv` de Python:

```bash
# Crear un entorno virtual:
python -m venv venv

# Activar el entorno virtual:
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate    
```

Luego de activar el entorno virtual, puedes instalar las dependencias necesarias para tu proyecto.

## Tkinter:
```bash
# Para instalar Tkinter, generalmente no es necesario instalarlo por separado, ya que viene incluido con la mayoría de las instalaciones de Python. Sin embargo, si necesitas instalarlo manualmente, puedes usar el siguiente comando:
sudo apt install python3-tk

# Descargar custom tkinter:
pip install customtkinter
```

## Graphviz:
```bash
# Descargar Graphviz:
pip install graphviz
```

> CustomTheme de customtkinter:
> https://github.com/TomSchimansky/CustomTkinter/blob/master/customtkinter/assets/themes/dark-blue.json