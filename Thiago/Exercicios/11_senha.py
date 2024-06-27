"""
Descrição: Faça um programa que solicite para o usuário a senha de acesso 
ao sistema , ele terá no máximo três tentativas para inserir a correta
cadastrada (senai115), caso passe desse limite uma mensagem de erro deve aparecer
"""

senha = "senai115"
tentativas = 3

# Iniciamos o loop dizendo que tentativas é maior que 0 , verificando se tentativas é maior que zero. No tentativas -= 1 
# ele desconta cada número de tentativa , assim ele para de rodar o loop quando chega a zero 
while tentativas > 0:
    senha_ = input("Digite a senha do usuário: ")

    # Verificamos se a senha é a verdadeira do usuário 
    if senha_ == senha:
        print("Seja bem-vindo !")
        break # Aqui ele encerra o loop
    else:
        print("Acesso negado Tente novamente >>> ")
        tentativas -= 1 # Aqui ele vai descontando o número de tentativas que o usuario teve 

if tentativas == senha: 
    print("Error !!!")    
elif tentativas < 3: # Aqui ele comunica para o usuário que excedeu suas tentatias e encerra o código !
    print("Você excedeu suas tentativas !")
