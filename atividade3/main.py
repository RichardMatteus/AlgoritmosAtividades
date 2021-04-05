from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Moto import Moto
from Carro import Carro

print('------VEICULO-----')
v1 = Veiculo('Fiat', 4, 'Uno', 65)
v1.imprimirInformacoes()
v1.acelerar(10)
v1.frear(50)
print('')

print('------BICICLETA-----')
b1 = Bicicleta('Caloi',2,'BMX',25,27,'não')
b1.imprimirInformacoes()
print('')

print('------AUTOMOVEL-----')
a1 = Automovel('Ford',4,'Mustang',120,466)
a1.imprimirInformacoes()
print('')

print('------MOTO-----')
m1 = Moto('Honda',2,'Biz 125',40,15, 'sim')
m1.imprimirInformacoes()
print('')

print('------CARRO-----')
c1 = Carro('Chevrolet',4,'Camaro',110,461,2)
c1.imprimirInformacoes()
print('')