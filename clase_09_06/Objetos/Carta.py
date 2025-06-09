class Carta():
    def __init__(self, color, valor):
        self.color = color
        self.valor = valor

    def __str__(self):
        return f"{self.color} {self.valor}"