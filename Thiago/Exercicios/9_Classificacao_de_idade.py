"""
Descrição: Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que pertence, de acordo com a tabela abaixo

    Faixa Etária:   Classificação:
    < 12            Criança
    13 ~ 17         Adolescente
    18 ~ 59         Adulto
"""

idade = int(input("Qual sua idade: "))

if idade <= 12:
    print("Criança")
elif idade >= 13 and idade < 17:
    print("Adolescente")
else:
    print("Adulto")