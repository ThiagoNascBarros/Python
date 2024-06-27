"""
Descrição: Escreva um programa que leia a velocidade máxima permitida em uma avenida e velocidade com que o motorista 
estava dirigindo nela e calcule a multa que uma pessoa vai receeber;

    Velocidade Ultrapassada:    Valor da multa: 
    Até 10 Km/h                 R$ 50,00
    11 a 30 Km/h                R$ 100,00
    Mais 31 Km/h                R$ 150,00
"""
velocidadeMaxima = 0
velocidadeDoMotorista = 0

velocidadeMaxima = float(input("Qual é a velocidade máxima da avenida: "))
velocidadeDoMotorista = float(input("Qual foi a velocidade do motorista: "))

velocidade_ultrapassada = velocidadeDoMotorista - velocidadeMaxima

if velocidade_ultrapassada >= 0 and velocidade_ultrapassada <= 10:
    print("Multa de R$ 50,00")
elif velocidadeDoMotorista >= 11 and velocidadeDoMotorista < 30:
    print("Multa de R$ 100,00")    
else:
    print("Multa de R$ 150,00")    