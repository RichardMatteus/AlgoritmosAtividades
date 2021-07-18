from No import No

class Lista:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionarNoInicio(self, valor):
        no = No(valor)
        if self.tamanho == 0 :
            self.inicio = no
            self.fim = no
        else:
            aux = self.inicio
            no.proximo = aux
            aux.anterior = no
            self.inicio = no
        self.tamanho +=1

    def adicionarNoFim(self, valor):
        no = No(valor)
        if self.tamanho == 0 :
            self.inicio = no
            self.fim = no
        else:
            aux = self.fim
            no.anterior = aux
            aux.proximo = no
            self.fim = no
        self.tamanho +=1

    def imprimir(self):
        if self.tamanho == 0 :
            print("Lista Duplamente Encadeada Vazia!")
        texto = ""
        aux = self.inicio
        while(aux) :
            texto += str(aux.dado) + " --> "
            aux = aux.proximo
        print( texto )
        print( "Tamanho da Lista Duplamente Encadeada: " + str(self.tamanho))

    def imprimirReverso(self):
        if self.tamanho == 0 :
            print("Lista Duplamente Encadeada Vazia!")
        texto = ""
        aux = self.fim
        while( aux ) :
            texto += str(aux.dado) + " --> "
            aux = aux.anterior
        print( texto )
        print( "Tamanho da Lista Duplamente Encadeada: " + str(self.tamanho))

    def removerDoInicio(self):
        if self.tamanho == 0 :
            print("Lista Duplamente Encadeada Vazia!")
        elif self.tamanho == 1 :
            self.inicio = None
            self.fim = None
            self.tamanho = 0
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
            self.tamanho -= 1

    def removerDoFim(self):
        if self.tamanho == 0 :
            print("Lista Duplamente Encadeada Vazia!")
        elif self.tamanho == 1 :
            self.inicio = None
            self.fim = None
            self.tamanho = 0
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
            self.tamanho -= 1
    
    
            



