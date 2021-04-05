from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, partidaEletrica):
        Automovel.__init__(self,marca,qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.partidaEletrica = partidaEletrica

    def imprimirInformacoes(self):
        print('O veículo cadastado é da marca %s, possue %s rodas e seu modelo é %s. Sua velocidade é de %s Km/h e seu motor possui %scv de potencia. Essa moto %s partida eletrica. ' % (self.marca,self.qtdRodas,self.modelo,self.velocidade,self.potenciaDoMotor,Moto.possuePartidaEletrica(self)))

    def possuePartidaEletrica(self):
        if self.partidaEletrica.upper() =='SIM':
            return 'possue'
        else:
            return 'não possue'