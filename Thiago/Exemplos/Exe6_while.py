"""
Autor: Thiago
Data: 07/06/2024
Descrição: Estudo da estrutura de repetição "While" 
# """
# indice = 1
# while indice < 16:
#     print("Indice: ", indice)
#     indice += 1

# print("\n")S

# indice2 = 10
# while indice2 > 0:
#     print("Thiago ", indice2)
#     indice2 += -1


# indice_3 = 1
# while True:
#     print(indice_3)
#     indice_3 = indice_3 + 1
#     if indice_3 == 5:
#         break

# op = 1
# while True:
#     opcao = input("Digite S para finalizar o programa: ")
#     op += 1
#     if opcao == "S" or opcao == "s":
#         break

senha = 1
while True:
    senha_ = input("Digite a senha do usuário: ")
    senha += 1
    if senha_ == "senai115":
        print("Seja bem-vindo !")
        break
    else: 
        print("Acesso negado \n Tente novamente \n >>> ")