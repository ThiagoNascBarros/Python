'''
Algoritmo "Média turma"
Descrição   : Faça um programa que receba duas notas de seis alunos. 
                Calcule e mostre:
            	A média aritmética das duas notas de cada aluno; e
            	A mensagem que está na tabela a seguir:
                    Média Aritmética	Mensagem
                    Até 3	            Reprovado 
                    Entre 4 e 7 	    Exame
                    De 8 para cima	    Aprovado

            	O total de alunos aprovados;
            	O total de alunos de exame;
            	O total de alunos reprovados;
            	A média da classe.
'''

qtdAlunos = 6
aluno = 0 
alunos_aprovados = 0
alunos_reprovados = 0
alunos_exame = 0
somaMedia = 0 # De primeira o código não rodou por que esta variavel não recebeu nenhum valor

while aluno < qtdAlunos:
    aluno = aluno + 1 # Decremento !
    nota_um = 0
    nota_dois = 0
    media = 0
    nota_um = float(input("Digite a nota 1 do aluno {}: ".format(aluno)))
    nota_dois = float(input("Digite a nota 2 do aluno {}: ".format(aluno)))

    media = (nota_um + nota_dois) / 2
    somaMedia = somaMedia + media
    if media <= 10:
        if media <= 3:
            print("Reprovado !!!")
            alunos_reprovados = alunos_reprovados + 1
        elif media >= 4 and media <= 7:
            print("Exame !")
            alunos_exame = alunos_exame + 1 # Decremento
        else:
            print("Aprovado !!!!")
            alunos_aprovados = alunos_aprovados + 1 # Decremento
    else:
        print("Nota inválida ! \nInsira uma nota válida de 1 á 10 !\n Está nota será nula e não contara para média da classe !")

mediaFinal = round(somaMedia / qtdAlunos)

print("===================================")

print("\nQuantidade de alunos aprovados: {}".format(alunos_aprovados))
print("\nQuantidade de alunos reprovados: {}".format(alunos_reprovados))
print("\nQuantidade de alunos no Exame : {} \n".format(alunos_exame))
print("\nA média final da classe foi de --> {:.2f}".format(mediaFinal))

print("===================================")
