import customtkinter as ctk

from utils import leer_archivo, generar_reporte, mover_posicion

# apariencia y tema:
ctk.set_appearance_mode("Dark") # Light, Dark, System
ctk.set_default_color_theme("blue") # blue, green, dark-blue

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurar una ventana:
        self.title("Ejemplo con CustomTKINTER")
        self.geometry("1280x720")

        # Etiqueta:
        self.label = ctk.CTkLabel(self, text="¡Hola! Esta es una app realizada con customTkinter", font=("Arial", 24))
        self.label.pack(pady=20)

        # Boton 1
        self.button1 = ctk.CTkButton(self, text="Configurar", width=400, height=80, font=("Arial", 18), command=self.on_button1_click)
        self.button1.place(relx=0.2, rely=0.5, anchor="center")

        # Boton 2
        self.button2 = ctk.CTkButton(self, text="Iniciar", width=400, height=80, font=("Arial", 18), command=self.on_button2_click)
        self.button2.place(relx=0.8, rely=0.5, anchor="center")

    def on_button1_click(self):
        fileOpen = ctk.filedialog.askopenfilename(title="Selecciona un archivo de entrada: ", filetypes=[("Archivo de entrada", "*.xml")])

        if fileOpen:
            self.label.configure(text=f"Archivo seleccionado: {fileOpen}")
            self.LeerArchivo(archivo=fileOpen)

    def LeerArchivo(self, archivo):
        try:
            with open(archivo, 'r') as file:
                verificar = leer_archivo(archivo)
                if verificar:
                    self.label.configure(text=f'Archivo leído correctamente.')
                else:
                    self.label.configure(text=f'Error al leer el archivo, puede que no se hayan encontrado las cartas.')
        except FileNotFoundError:
            self.label.configure(text=f'Archivo no encontrado: {archivo}')

        except Exception as e:
            self.label.configure(text=f'Error al leer el archivo - {e}')


    def on_button2_click(self):
        # Abrir una subventana:
        self.subwindow = ctk.CTkToplevel(self)
        self.subwindow.title("Ventana de aplicacion")
        self.subwindow.geometry("1280x720")

        self.input_label = ctk.CTkLabel(self.subwindow, text="Ingrese un número:", font=("Arial", 18))
        self.input_label.pack(pady=20)
        self.input_entry = ctk.CTkEntry(self.subwindow, width=200, font=("Arial", 18))
        self.input_entry.pack(pady=10)

        self.shuffle_button = ctk.CTkButton(self.subwindow, text="Mover", width=200, height=50, font=("Arial", 18), command=lambda: mover_posicion(int(self.input_entry.get())))
        self.shuffle_button.pack(pady=20)

        self.boton_reporte = ctk.CTkButton(self.subwindow, text="Generar Reporte", width=200, height=50, font=("Arial", 18), command=generar_reporte)
        self.boton_reporte.pack(pady=40)



if __name__ == "__main__":
    app = App()
    app.mainloop()
    print("Hola estoy ejecutando mi app.")