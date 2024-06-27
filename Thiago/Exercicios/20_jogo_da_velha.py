"""
Descrição: Faça um jogo da velha
"""


tab = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
      ]
rodadas = 0
chances = 0
jogador = 'X'
while chances < 9:
    posicao = input(f'Jogador {jogador} escolha uma posição: ')
    posicao_encontrada = False
    for linha in range(3):
        linha_completa = ''
        for coluna in range(3):
            if posicao == tab[linha][coluna]:
                tab[linha][coluna] = jogador
                posicao_encontrada = True
            linha_completa += tab[linha][coluna] + ' | '
        print(linha_completa)
    if posicao_encontrada == True:
        rodadas = rodadas + 1   
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'
    else:
        print('Posição não encontrada')