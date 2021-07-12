class Autor:
    def __init__(self, id, nome):
        self.__id = id
        self.nome = nome

class Laco:
    def __init__(self, dado):
        self.dado = dado
        self.next = None
        
class Pilha:
    def _init_(self):
        self.topo = None
        self.range = 0

   
    def empilhar(self, elemento):
        laco = Laco(elemento)
        laco.next = self.topo
        self.topo = laco
        self.range += 1

    def remover(self):
        if self.range > 0:
            laco = self.topo
            self.topo = self.topo.next
            self.range -= 1
            return laco.dado
        print("A pilha está vazia")    

    def _tamanho_(self):
        return self.range

    def olhar(self):
        if self.range > 0:
            return self.topo.dado
        print("A pilha está vazia")

    def _reproduzir_(self):
        r = ""
        cursor = self.topo
        while cursor:
            r = r + str(cursor.dado) + "\n"
            cursor = cursor.proximo
        return r

    def _string_(self):
        return self._reproduzir_()