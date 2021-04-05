from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        print('A bicicleta cadastrada é da marca %s, possue %s rodas e seu modelo é %s. Sua velocidade é de %s Km/h. Ela possue %s marchas e %s bagageiro. ' % (self.marca,self.qtdRodas,self.modelo,self.velocidade,self.numMarchas,Bicicleta.possueBagageiro(self)))  

    def possueBagageiro(self):
        if self.bagageiro.upper() =='SIM':
            return 'possue'
        else:
            return 'não possue'