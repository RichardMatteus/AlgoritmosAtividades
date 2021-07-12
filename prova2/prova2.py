class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

class Autor:
    def __init__(self, id, nome):
        self.__id = id
        self.nome = nome

    def imprimir(self):
        print("Id do autor:", self.__id)
        print("Nome do autor:", self.nome)

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
    
a1 = Autor('1','Richard')
a2 = Autor('2','Ana')
a3 = Autor('3','Mauricio') 

a1.imprimir()
a2.imprimir()
a3.imprimir()

l1 = Livro('10','Sonho de Verão',a1.nome)
l2 = Livro('11','Sonho de Primavera',a2.nome)
l3 = Livro('12','Sonho de Outono',a3.nome)

pilha = Pilha()
pilha.empilha(l1.titulo)
pilha.imprimir()
input()
pilha.empilha(l2.titulo)
pilha.imprimir()
input()
pilha.empilha(l3.titulo)
pilha.imprimir()
input()
pilha.desempilha()
pilha.imprimir()
input()
pilha.desempilha()
pilha.imprimir()

