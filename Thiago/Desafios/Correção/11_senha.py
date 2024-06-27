# Váriveis
senha = "" # Var para receber a senha do usuário

senhaPadrao = "senai115"
tentativas = 3

while True:
    senha = input("Digite sua senha: ")
    
    if senha == senhaPadrao:
        print("Acesso liberado !")
        break # Quebra o loop , ou seja finaliza o programa !
    else:
        tentativas = tentativas - 1
        print("Acesso negado !!! \nVocê tem mais", tentativas, "tentativas !")
        break # Quebra o loop , ou seja finaliza o programa !

    if tentativas <= 0:
        print("Você excedeu seu número de tentativas !")
        break

