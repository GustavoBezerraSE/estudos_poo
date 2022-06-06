from classes import *

"""
Associação - Usa / Agregação - Tem / Composição - é dono / Herança - É
"""

c1 = Cliente('Luiz', 45)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 54)
a1.falar()
a1.estudar()

c2 = ClienteVIP('Gustavo', 20, 'Bezerra')
c2.falar()
