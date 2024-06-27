# =================================================================
# Autor: Thiago Nascimento
# Data: 24/05/2024
# Versão: 1.0
# Descrição: Faça um algoritmo que receba cinco notas e imprima 
#            a média final do aluno  
# ------------------------------------------------------------------
#            Exeplo de execução 
#            Nota 1: 10
#            Nota 2: 10
#            Nota 3: 10
#            Nota 4: 10
#            Nota 5: 10
#            Média Final: 10
# =================================================================

# Entrada
nota1 = int(input("Qual foi a primeira nota do aluno : ")) # Se não tiver esse -> int na frente de input ele apenas contatena e compreende que a variavel é string
nota2 = int(input("Qual foi a segunda nota do aluno : "))
nota3 = int(input("Qual foi a terceira nota do aluno : "))
nota4 = int(input("Qual foi a quarta nota do aluno : "))
nota5 = int(input("Qual foi a quinta nota do aluno : "))

# Processamento
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5 # Se não tiver os parenteses na soma na ultima soma ele vai soma a nota5 divida por cinco, como o usuario entrou com 10 na nota5 assim ele ficaria com 5 e daria um error de syntaxe.

# Saída
print("A média do aluno foi de ", media)
if media >= 7:
    print("O aluno foi Aprovado !")
else:
    print("O aluno foi Reprovado !")

