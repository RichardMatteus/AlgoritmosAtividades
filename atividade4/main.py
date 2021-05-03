class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimeNome(self):
        print(self.nome)

    def __imprimeTelefone(self):
        print(self.__telefone)


p1 = Pessoa(1, 'Richard', 'Santana', '3333333')
p1.imprimeNome()
p1.__imprimeTelefone()

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self,codigo,nome,endereco,telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprimeCPF(self):
        print(self.__cpf)

    def __calculaIMC(self):
        imc = self.peso/self.altura**2
        print(round(imc, 2))
    
f1 = Fisica(2, 'Joao', 'POA', '222222', '879879854', 20, 70, 1.74)
f1.imprimeCPF()
f1.__calculaIMC()

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, CNPJ, inscricaoEstadual, quantidadeFuncionarios):        
        Pessoa.__init__(self,codigo,nome,endereco,telefone)
        self.__CNPJ = CNPJ
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def imprimeCNPJ(self):
        print(self.__CNPJ)

    def emitirNotaFiscal(self):
        print('Nota fiscal emitida')

j1= Juridica(1, 'Marcos', 'Canoas', '1111111','2175615945',2131574,40)
j1.imprimeCNPJ()
    
