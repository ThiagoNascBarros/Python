"""
Descrição: Faça um programa que adicione alunos no sistema da escola
           (Array) ou remova um aluno especifico.
           Nesse sistema deve estar previsto um menu com três opções:
           ==========================
           Sistema SENAi
           1) Adicionar aluno:
           2) Remover aluno:
           3) Apresentar alunos
           4) Sair
           ==========================
           Adicionar aluno 
           Insira o nome do aluno:
           ==========================
           Alunos no sistema
           ["João", "Pedro"]
           ==========================
           Remover aluno
           Insira o nome do aluno para ser removido:
           ==========================
"""
import os
varUsr = []


while True:
    print("============ Sistema SENAI ============\n1) Adicionar aluno\n2) Remover aluno\n3) Apresentar alunos\n4) Sair")
    varEscUsr = input("Digite sua escolha: ")

    if varEscUsr == '1':
        os.system('cls') # Limpar o terminal
        print("Os usuários -->", varUsr)
        varUsr.append(input("Digite o nome do aluno que queira adicionar: "))
        print(varUsr)
    elif varEscUsr == '2':
        os.system('cls') # Limpar o terminal
        print("Os usuários -->", varUsr)
        varUsr.remove(input("Digite o nome do aluno que queira remover: "))
    elif varEscUsr == '3':
        os.system('cls') # Limpar o terminal
        print("==========================================")
        print(varUsr)
        print("==========================================") 
    elif varEscUsr == '4':
        break