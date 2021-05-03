from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        Computador.__init__(self, modelo, cor, preco)
        self.potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        print('Seu Desktop é um %s %s que custou R$ %s. Sua fonte tem %sW de potencia. ' % (self.modelo, self.cor, self.preco, self.potenciaDaFonte))

