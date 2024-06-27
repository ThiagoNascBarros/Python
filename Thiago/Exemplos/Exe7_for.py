"""
Autor: Thiago
Data: 13/06/2024
Descrição: Estudo da estrutura de repetição "For"


"""
indice_um = 1
indice_dois = 1

# ======================
while indice_um < 6:
    print("Indice", indice_um)
    indice_um += 1
# ======================
print("\n=====================")
print("\n")
# ======================
for indice_dois in range(6):
    print("Indice", indice_dois)
# ======================    
for indice_dois in range(1, 6): # Aqui ele começa em um Exemplo --> "range(1 , 6)" "range(1, 7)"
    print("Indice", indice_dois)