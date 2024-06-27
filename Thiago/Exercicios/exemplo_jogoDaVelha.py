# Jogo da Velha sem funções definidas em Python

# Inicialização do tabuleiro vazio
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

jogador_atual = "X"  # Começa com o jogador X

# Loop principal do jogo
while True:
    # Imprimir tabuleiro
    for linha in tabuleiro:
        print("|".join(linha))
        print("-----")
    
    # Captura da posição desejada pelo jogador
    linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): "))
    coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): "))
    
    # Verificação se a posição está vazia
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador_atual
    else:
        print("Posição ocupada. Escolha outra.")
        continue
    
    # Verificação de vitória
    # Verifica se há vitória na linha
    for linha in tabuleiro:
        if linha.count(jogador_atual) == 3:
            # Imprimir tabuleiro final
            for linha in tabuleiro:
                print("|".join(linha))
                print("-----")
            print(f"Jogador {jogador_atual} venceu!")
            quit()

    # Verifica se há vitória na coluna
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] == jogador_atual:
            # Imprimir tabuleiro final
            for linha in tabuleiro:
                print("|".join(linha))
                print("-----")
            print(f"Jogador {jogador_atual} venceu!")
            quit()

    # Verifica se há vitória na diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador_atual:
        # Imprimir tabuleiro final
        for linha in tabuleiro:
            print("|".join(linha))
            print("-----")
        print(f"Jogador {jogador_atual} venceu!")
        quit()

    # Verifica se há vitória na diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador_atual:
        # Imprimir tabuleiro final
        for linha in tabuleiro:
            print("|".join(linha))
            print("-----")
        print(f"Jogador {jogador_atual} venceu!")
        quit()

    # Verifica se há empate
    if all(all(pos != " " for pos in linha) for linha in tabuleiro):
        # Imprimir tabuleiro final
        for linha in tabuleiro:
            print("|".join(linha))
            print("-----")
        print("Empate!")
        quit()
    
    # Alternância de jogador
    jogador_atual = "O" if jogador_atual == "X" else "X"
