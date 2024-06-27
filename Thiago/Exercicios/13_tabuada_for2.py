"""
Autor: Thiago
Data: 13/06/2024
Algoritmo: "Tabuada 1 ao 9"
Descrição: Faça um programa que apresente a tabuada 1 ao 10
"""

tabuada = 1

for num in range(11):
    print("======================")
    print("A tabuada do número {}".format(num))
    print("======================")
    for tabuada in range(11):
        tab = num * tabuada
        print("{} x {} = {}".format(num, tabuada, tab))
print("======================")