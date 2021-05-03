from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook

print('Computador')
c1 = Computador("HP", 'Preto', 2900)
c1.cadastrar()
c1.getInformacoes()

print('Desktop')

d1 = Desktop('Dell','Branco', 4700, 650)
d1.getInformacoes()

print('Notebook')

n1 = Notebook('Lenovo', "Rosa", '3250', '2:00')
n1.getInformacoes()