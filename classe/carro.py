'''Implemente uma classe chamada Carro com as seguintes propriedades:
a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível
no tanque.
b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de
combustível no tanque de gasolina.
d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:'''


class Carro():
    def __init__(self, marca, modelo, consumo):
        self.marca = marca
        self.modelo = modelo
        self.consumo = consumo
        self.tanque = 0

    def obter_gasolina(self):
        print(f'O veículo {self.marca + " " + self.modelo} está com {self.tanque:.2f} litros de combustível.')

    def adicionar_gasolina(self, qtd):
        self.tanque += qtd

    def andar(self, km):
        if self.tanque == 0:
            print(f'O veículo {self.marca + " " +self.modelo} não possuí combustível suficiente.')
        else:
            if self.tanque > (km / self.consumo):
                self.tanque -= km / self.consumo
                print(f'O veículo {self.marca + " " + self.modelo} consumiu '
                      f'{km / self.consumo:.2f} litros para andar {km} km.')
            else:
                km_percorrido = self.tanque * self.consumo
                self.tanque = 0
                print(f'O veículo {self.marca + " " +self.modelo} '
                      f'ficou sem combustível após percorrer {km_percorrido:.2f} km.')


c1 = Carro('Ford', 'KA', 14.7)
c1.adicionar_gasolina(20)
c1.andar(14)
c1.andar(400)
c1.obter_gasolina()
