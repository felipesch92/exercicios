class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setCor(self, cor):
        self.cor = cor

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getCor(self):
        return self.cor


carro1 = Carro('Fiat', 'Mobi', 'Branco')
print(carro1.getCor())