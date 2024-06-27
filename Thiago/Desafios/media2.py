# Interpolação ---> "Misturar" Strings com váriaveis.
#  Exeplo: print("joao {}".format(nome))
# Exemplo: print(f"joao {nome}")

qtdAlunos = 6
aluno = 0 
alunos_aprovados = 0
alunos_reprovados = 0
alunos_exame = 0
 
while aluno < qtdAlunos:
    aluno = aluno + 1 # Decremento !
    nota_um = 0
    nota_dois = 0
    media = 0
    nota_um = float(input("Digite a nota 1 do aluno {}: ".format(aluno)))
    nota_dois = float(input("Digite a nota 2 do aluno {}: ".format(aluno)))

    media = (nota_um + nota_dois) / 2

    if media <= 3:
        print("Reprovado !!!")
        alunos_reprovados = alunos_reprovados + 1
    elif media >= 4 and media <= 7:
        print("Exame !")
        alunos_exame = alunos_exame + 1
    else:
        print("Aprovado !!!!")
        alunos_aprovados = alunos_aprovados + 1

print("\nQuantidade de alunos aprovados: {}".format(alunos_aprovados))
print("\nQuantidade de alunos reprovados: {}".format(alunos_reprovados))
print("\nQuantidade de alunos no Exame : {} \n".format(alunos_exame))