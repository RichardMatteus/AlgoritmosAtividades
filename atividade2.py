#Construa um algoritmo para implementar a classe Aluno que contém os atributos código, nome e matrícula. 
#A classe Aluno possui duas subclasses, sendo a classe AlunoEnsinoMedio, 
#que tem o atributo ano como seu atributo próprio e a classe AlunoGraduacao que tem o atributo semestre como atributo próprio. 
#As duas subclasses herdam todos atributos da classe Aluno. 
#As três classes possuem o método construtor e também o método imprimir, 
#que imprime na tela os valores de todos os atributos da sua respectiva classe.

class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

class AlunoEnsinoMedio(Aluno):
    def __init__(self,codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano
        print('Aluno %s cadastrado com sucesso. ' % (self.nome))
    
    def imprimir_EnsinoMedio(self):
        print('Aluno: %s \nCodigo: %s \nMatricula: %s \nAno: %s' % (self.nome,self.codigo,self.matricula,self.ano))

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre
        print('Aluno %s cadastrado com sucesso. ' %(self.nome))

    def imprimir_Graduacao(self):
        print('Aluno: %s \nCodigo: %s \nMatricula: %s \nSemestre: %s' % (self.nome,self.codigo,self.matricula,self.semestre))


p1 = AlunoEnsinoMedio('1','Carlos','15654','5')
p1.imprimir_EnsinoMedio()
p2 = AlunoGraduacao(2,'Joao',45,8)
p2.imprimir_Graduacao()
