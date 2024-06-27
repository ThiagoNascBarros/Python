''' 
Abertura comentário

Autor : Thiago Nascimento
Data: 28/05/24
Versão: 1.0
Descrição: Estudos de condicional IF ... ELSE

Fechamento comentário
'''

# Entrada
notas = [int(input("Qual a nota 1 ? ")), int(input("Qual a nota 2 ? ")), int(input("Qual a nota 3 ? ")), int(input("Qual a nota 4 ? ")), int(input("Qual a nota 5 ? "))]
# Processamento
media = float(notas[0] + notas[1] + notas[2] + notas[3] + notas[4]) / 5
# Saída
print(media)
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")