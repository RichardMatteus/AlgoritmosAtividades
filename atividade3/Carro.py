from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortas):
        Automovel.__init__(self, marca,qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.qtdPortas = qtdPortas

    def imprimirInformacoes(self):
        print('O veículo cadastado é da marca %s, possue %s rodas, %s portas e seu modelo é %s. Sua velocidade é de %s Km/h e seu motor possui %scv de potencia. ' % (self.marca,self.qtdRodas,self.qtdPortas,self.modelo,self.velocidade,self.potenciaDoMotor))