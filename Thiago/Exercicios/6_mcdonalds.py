'''
Descrição: Escreva um algoritmo para exibir o nome do lanche de acordo do número insirido pelo usuário, seguindo a tabela abaixo:

Nr:
1 Big mac 
2 Quarteirão
3 McChicken 
4 Cheddar McMelt
5 McFish

'''

lanche = int(input("Bem vindo ao McDonalds \n Qual lanche você quer ? \n 1. Big mac \n 2. Quarteirão \n 3. McChicken \n 4. CheddarMcMelt \n 5. McFish \n"))

if(lanche == 1):
    print("O preço desde lanche é de R$ 5,78")
elif(lanche == 2):
    print("O preço desde lanche é de R$ 5,58")
elif(lanche == 3):
    print("O preço desde lanche é de R$ 5,68")
elif(lanche == 4):
    print("O preço desde lanche é de R$ 5,99")
else:
    print("O preço desde lanche é de R$8,00")