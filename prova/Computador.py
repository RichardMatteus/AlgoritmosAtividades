from abc import ABCMeta, abstractmethod

class Computador:
    __metaclass__ = ABCMeta
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    @abstractmethod
    def cadastrar(self):
        print('Computador cadastrado com sucesso. ')

    def getInformacoes(self):
        print('Seu computador é um %s %s que custou R$ %s. ' % (self.modelo, self.cor, self.preco))