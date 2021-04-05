class Veiculo():
    def __init__(self, marca, qtdRodas, modelo, velocidade):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirInformacoes(self):
        print('O veículo cadastado é da marca %s, possue %s rodas e seu modelo é %s. Sua velocidade é de %s Km/h. ' % (self.marca,self.qtdRodas,self.modelo,self.velocidade))

    def acelerar(self,valor):
        print('Sua velocidade apos acelerar é de: %s Km/h.' % (valor+self.velocidade))

    def frear(self,valor):
        print('Sua velocidade apos frear é de: %s Km/h.' % (self.velocidade-valor))