"""
Autor: Thiago
Data: 17/06/24
Descrição: Estudo do tipo de dado Array
"""

cars = ["Vw"]
cars.append("Gm")   # Adiciona na ultima posição o valor indicado 
cars.append("Ford")
cars.append("Fiat")
cars.append("Renault")

print(cars)

cars.remove('Ford') # Remove item indicando o valor 
print(cars)

cars.pop(int(input("Digite o indice: "))) # Para remover o Renalt usando o indice
print(cars)

print(len(cars)) # Tamanho do Array atual 
print(cars)
cars.pop(len(cars) - 1) # Deleta sempre a última posição do Array
print(cars) 