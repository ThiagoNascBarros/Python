# alunos_python_noturno = ["Davi", "Felipe", "Bruno", "José", "João", "Mauricio", "Aldivan", "Danielle", "Luana", "Gustavo", 
#                          "Arthur", "Pedro", "Kawan", "Andrey", "Lucas", "Diego", "Ana", "Vinicius", "Adriel", "Patrick", "Professor Julião"]

# alunoSelect = int(input("Número da chamada do aluno: "))

# print(alunos_python_noturno[alunoSelect])

while True:
    alunos_python_noturno = ["Davi", "Felipe", "Bruno", "José", "João", "Mauricio", "Aldivan", "Danielle", "Luana", "Gustavo", 
                         "Arthur", "Pedro", "Kawan", "Andrey", "Lucas", "Diego", "Ana", "Vinicius", "Adriel", "Patrick", "Professor Julião"]

    alunoSelect = int(input("Número da chamada do aluno: "))
    print(alunos_python_noturno[alunoSelect])

    continuar_User = input("Deseja continuar ?\nS | n\n--> ")
    if continuar_User == "n":
        break
    else:
        continue
