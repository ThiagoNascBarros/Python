"""
Descrição: Calcular o indíce de massa do corpo !

Abaixo de 18.5 (Abaixo do peso)
Entre 18,6 e 24,9 (Peso ideal)
Entre 25,0 e 29,9 (Levemente acima do peso)
Entre 30,0 e 34,9 (Obesidade Grau I)
Entre 35,0 e 39,9 (Obesidade Grau II)
Acima de 40 (Obesidade III)

Fórmula : peso (kg) ÷ (altura x altura) (m)

"""

peso = float(input("Qual seu peso ? "))
altura = float(input("Qual sua altura ? "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso !!!")
elif imc > 18.6 and imc <= 24.9:
    print("Peso ideal")
elif imc > 25.0 and imc <= 29.9:
    print("Levemente acima do peso !")
elif imc > 30.0 and imc <= 34.9:
    print("Obesidade Grau I")
elif imc > 35.0 and imc <= 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")