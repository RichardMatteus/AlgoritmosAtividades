from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimirInformacoes(self):
        print('O veículo cadastado é da marca %s, possue %s rodas e seu modelo é %s. Sua velocidade é de %s Km/h e seu motor possui %scv de potencia. ' % (self.marca,self.qtdRodas,self.modelo,self.velocidade,self.potenciaDoMotor))
