''' 
Abertura comentário

Autor : Thiago Nascimento
Data: 28/05/24
Versão: 1.0
Descrição: Estudos de condicional ELIF

Fechamento comentário
'''

# =========================================
# Variavel
nota = 0
# Entrada
nota = int(input("Digite a nota: ")) # Esse "int" se chama casting , por que quem escreveu o código quer que a entrada do usuário seja de número inteiro(int) 
# Processamento
if(nota >= 6):
    print("Aprovado !")
elif(nota < 4): 
    print("Reprovado !")
else:
    print("Recuperação !")
# =========================================