"""
Autor: Thiago
Data: 25/06/2024
Descrição: Estudo do tipo array (vetor)
"""

# alunosSala = ['Luana', 'Gustavo', 'Thiago']
# alunosSala.append('Felipe')
# # print(alunosSala)

# # alunosSala[2] # Indice 2 --> Thiago
# # print(alunosSala[2]) # Mesma coisa 

# # for indice in range(4):
# #     print(alunosSala[indice])

# for aluno in alunosSala:
#     print(aluno)


cabecalho = ['Nome', 'Idade', 'Matricula']

dado_um = ['Pelé', 'Eterno', '10']

# Matriz --> um array com arrays dentro
tabela = [cabecalho, dado_um]


# Coordenadas [l][c] l = Linha , c = Coluna 
print(tabela[1][0]) # ---> Pelé

# [      0        1         2
# 0    ['Nome', 'Idade', 'Matricula'],
# 1    ['Pele', 'Eterno', '10']
# ]
print(tabela[1][2]) # ---> 10