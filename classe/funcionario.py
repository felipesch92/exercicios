'''Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um
double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva
um pequeno programa que teste sua classe.
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o
salário do funcionário em uma certa porcentagem.'''

class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar(self):
        print(f'Funcionário: {self.nome}')
        print(f'Salário: {self.salario:.2f}')

    def aumentar_salario(self, a):
        self.salario += self.salario * (a / 100)


f1 = Funcionario('Felipe', 5500)
f1.aumentar_salario(15)
f1.aumentar_salario(10)
f1.mostrar()
