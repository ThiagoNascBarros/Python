# =================================================================
# Autor: Thiago Nascimento
# Data: 24/05/2024
# Versão: 1.0
# Descrição: 
#             Faça um algoritmo que receba o raio em metros 
#             de um circulo e apresente a sua área
# -----------------------------------------------------------------
#            Exemplo: 
#            Insira o raio em metros: 5
#            Área do circulo: 78.5m^2
# -----------------------------------------------------------------
#            a = área
#            pi = 3.14
#            r = raio 
#            a = pi*(r^2)
# =================================================================


area = 0
r = 0
pi = 3.14
r = int(input("Qual o raio do circulo ? ")) # Esse processo "int(input("Qual o raio do circulo ? "))" se chama cast

area = pi * (r**2)

print(area)