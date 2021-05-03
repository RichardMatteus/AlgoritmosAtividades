from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        Computador.__init__(self, modelo, cor, preco)
        self.tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        print('Seu Notebook é um %s %s que custou R$ %s. Sua bateria dura cerca de %sHrs. ' % (self.modelo, self.cor, self.preco, self.tempoDeBateria))