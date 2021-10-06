class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.ponto = 0
        self.escolha = ""

    def escolher(self):
        self.escolha = input("{nome}, escolha pedra, papel ou tesoura: ".format(nome=self.nome))
        print("{nome} selecionou {escolha}".format(nome=self.nome, escolha=self.escolha))

    #self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
    #print("{name} selects {choice}".format(name=self.name, choice = self.choice))


class Rodadas:
    def __init__(self, p1, p2):
        p1.escolher()
        p2.escolher()

    def comparar(self):
        print("implementar")

    def premioPontos(self):
        print("implementar")


class Jogo:
    def __init__(self):
        self.fimDeJogo = False
        self.jogador = Jogador("Felipe")
        self.segundoJogador = Jogador("Tamara")

    def iniciar(self):
        rodadas = Rodadas(self.jogador, self.segundoJogador)

    def verificarFinalCondicao(self):
        print("implementar")

    def determinarVencedor(self):
        print("implementar")


jogo = Jogo()
jogo.iniciar()

