class Times:
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado

class Pilha(object):
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):
        self.dados.append(elemento)
 
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0
 
    def imprimir(self):
        if len(self.dados) == 0:
            print('Pilha vazia.')
        else:
            print(self.dados)

############################

t1 = Times('Grêmio','RS')
t2 = Times('Internacional','RS')
t3 = Times('Santos','SP')
t4 = Times('Vasco','RJ')

pilha = Pilha()

pilha.empilha(t1.nome)
pilha.imprimir()
input()
pilha.empilha(t2.nome)
pilha.imprimir()
input()
pilha.empilha(t3.nome)
pilha.imprimir()
input()
pilha.desempilha()
pilha.imprimir()
input()
pilha.empilha(t4.nome)
pilha.imprimir()
input()
pilha.desempilha()
pilha.imprimir()
input()
