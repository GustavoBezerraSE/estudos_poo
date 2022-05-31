from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):                       #método de instancia
        print(self.ano_atual - self.idade)

    @classmethod                                           #não precisa da instancia mas precisa da classe em si
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod                                          #não precisa da instancia nem da classe em si
    def gera_id():                                         #como uma função normal mas por questão de organização
        rand = randint(10000,19999)                        #se coloca dentro da classse por exemplo
        return rand

p1 = Pessoa('Gustavo', 20)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())

