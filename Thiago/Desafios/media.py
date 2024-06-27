'''
Algoritmo "Média turma"
Descrição   : Faça um programa que receba duas notas de seis alunos. 
                Calcule e mostre:
            	A média aritmética das duas notas de cada aluno; e
            	A mensagem que está na tabela a seguir:
                    Média Aritmética	Mensagem
                    Até 3	            Reprovado 
                    Entre 3 e 7 	    Exame
                    De 7 para cima	    Aprovado

            	O total de alunos aprovados;
            	O total de alunos de exame;
            	O total de alunos reprovados;
            	A média da classe.
'''

# Váriaveis
alunos = 1
n1 = 0
n2 = 0
soma = 0

while alunos <= 6:
    n1 = int(input("Digite a primeria nota do aluno: "))
    n2 = int(input("Digite a segunda nota: "))
    
    media = (n1 + n2) / 2
    soma += media

    if media < 3:
        print("Aluno {} reprovado ! A sua média foi de {:.1f}".format(alunos, media))
    elif media > 4 and media < 7:
        print("Aluno {} foi para o exame ! Com a média de {:.1f}".format(alunos, media))
    elif media > 8:
        print("Aluno {} foi aprovado ! Sua média foi de {:.1f}".format(alunos, media))
        
    alunos += 1

print()