salario = 0

salario = float(input("Qual o salário do funcionário: "))


if salario < 1000: 
    novo__salario = salario + ((salario * 25) / 100) # Outra forma de fazer esse calculo é assim "novo__salario_ = salario * 1.25"
    aumento_de_salario = novo__salario - salario
    print("Aumento de 25% \n O funcionário passará a receber {:.1f} \n O aumento foi de {}".format(novo__salario, aumento_de_salario))
elif salario >= 1000 and salario < 2000:
    novo__salario_ = salario + ((salario * 15) / 100) # Outra forma de fazer esse calculo é assim "novo__salario_ = salario * 1.15"
    aumento_de_salario = novo__salario_ - salario
    print("Aumento de 15% \n O funcionário passará a receber {:.1f} \n O aumento foi de {}".format(novo__salario_, aumento_de_salario))    
elif salario >= 2000:
    novo__salario__ = salario + ((salario * 10) / 100) # Outra forma de fazer esse calculo é assim "novo__salario_ = salario * 1.10"
    aumento_de_salario = novo__salario__ - salario
    print("Aumento de 10% \n O funcionário passará a receber {:.1f} \n O aumento foi de {}".format(novo__salario__, aumento_de_salario))