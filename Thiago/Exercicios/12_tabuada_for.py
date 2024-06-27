'''
Nome: Thaigo
Algoritmo: Tabuada
Descrição: Faça um programa que calcule a tabuada de um número digitado
           pelo usuário.
'''

numDigitado = 0 # Declarando o valor zero para váriavel 
num = 0 # Declarando o valor zero para váriavel 
numDigitado = int(input("Digite o número deseja saber a tabuada: ")) # Entrada do usuário 


print("Tabuada de {}".format(numDigitado)) # Imprimir que tabuada irar ser apresentada
print("========================") # Divisão
for num in range(1, 11): # Laço que irar fazer o calculo do número digitado pelo usuário até dez
    resultadoTabuada = numDigitado * num # Multiplicando o numDigitado * num , o num irá representar os passos para frente. 
    # Exemplo: 1 -> 2 -> 3 -> 4 -> 5... até o número definido no "range"
    print("{} x {} = {}".format(numDigitado, num, resultadoTabuada)) # Apresentar na tela o resultado da tabuada 
    # Apresentar na tela usando a interpolação ".format()"
print("========================") # Divisão 