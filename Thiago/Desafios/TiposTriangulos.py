"""
Algoritmo: "Tipos de Triângulos "
Autor: Thiago
Data: 06/06/2024
Descrição: Faça um programa que recebe três valores e verifique se elas podem representar os lados
           em um triângulo. 
           
           1.Triângulo Escaleno ---> Quando o triângulo possui todos os lados com medidas diferentes !

           2.Triângulo Isósceles ---> Quando o triângulo possui dois lados de medidas iguais e um diferente !

           3.Triângulo Equilatero ---> Quando o triângulo possui todos os lados com medidas iguais !

           Lembrando que a soma das medidas de dois lados de um triângulo é sempre maior que a medida do terceiro lado !!!
"""

print("====================") 
ladoA = int(input("Digite o lado A do triângulo: "))
print("====================")   

ladoB = int(input("Digite o lado B do triângulo: "))
print("====================")   

ladoC = int(input("Digite o lado C do triângulo: ")) 



# "if a + b <= c or a + c <= b or b + c <= a:" --> Aqui ele vai comparar se os dois lados do triângulo é menor do que o terceiro lado

if ladoA + ladoB < ladoC or ladoA + ladoC < ladoB or ladoB + ladoC < ladoA or ladoA == 0 and ladoB == 0 and ladoC == 0:
    print("====================")
    print("Este triângulo não existe !")
    print("====================")
elif ladoA == ladoB and ladoB == ladoC:
    print("====================")   
    print("Triângulo Equilatero !")
    print("====================")
elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
    print("====================")
    print("Triâgulo Isósceles !")
    print("====================")
elif ladoA != ladoB and ladoB != ladoC:
    print("====================")
    print("Triângulo Escaleno !")        
    print("====================")
else:
    print("Error")