"""
Descrição: Faça um programa que receba dois valores , sendo que o primeiro
           deve ser menor que o segundo.
           O programa deve apresentar todos os números ímpares contidos nesta sequência.
           (Modulo %. Exemplo: 7%2 = 1)
"""

valorOne = int(input("Digite um valor: "))
valorTwo = int(input("Digite um segundo valor: "))
limite = 10

for i in range(valorOne, valorTwo + 1):
    if valorOne < valorTwo:
        if i % 2 != 0:
            print(i)
    

# limite = 10
# for numero in range(1, limite, 2):
#     print(numero)