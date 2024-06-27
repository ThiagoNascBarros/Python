"""
Descrição: Crie uma matriz e apresente ela no final da execução, aonde 
           existe duas colunas [Tipo, Nome] e 4 linhas preenchidas com
           o tipo do animal e seu respetivo nome.
"""

tabela = [
        ['#', 'Tipo', 'Nome'],
        ['0', 'Gato', 'Frajola'],
        ['1', 'Cão', 'Coragem'],
        ['2', 'Passarinho', 'Pica-pau'],
        ['3', 'Urso', 'Pooh']
]

for linha in range(5):
    linha_completa = ' '
    for coluna in range(3):
        linha_completa += tabela[linha][coluna] + ' | '
    print(f'{linha_completa}')