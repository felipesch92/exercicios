'''Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar
o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume
permanecem dentro de faixas válidas.'''


class TV:
    def __init__(self):
        self.canal = 0
        self.volume = 0

    def trocar_canal(self, n):
        if 0 < n < 51:
            self.canal = n
        else:
            print('Informe um canal entre 1 e 50!')

    def controlar_volume(self, cond):
        if cond.upper()[0] == 'A':
            if self.volume >= 100:
                print('Volume já esta no máximo!')
            else:
                self.volume += 1
        elif cond.upper()[0] == 'D':
            if self.volume < 1:
                print('Volume já esta no mínimo!')
            else:
                self.volume -= 1

    def mostrar(self):
        print('-' * 40)
        print(f'Canal: {self.canal}')
        print(f'Volume: {self.volume}')
        print('-' * 40)


tv1 = TV()
tv1.mostrar()
tv1.trocar_canal(51)
for x in range(0, 20):
    tv1.controlar_volume('a')
tv1.mostrar()
