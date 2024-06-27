# =================================================================
# Autor: Thiago Nascimento
# Data: 24/05/2024
# Versão: 1.0
# Descrição: 
#             
#              
# -----------------------------------------------------------------
#            Exemplo: Insira a temperatura em celsius: 0
#            Fahrenheit: 32ºF
#            Kelvin: 273,15 K
#            
# -----------------------------------------------------------------
# =================================================================


celsius = int(input("Quantidade em celsius para converter para fahrenheit: "))
conversaoFahrenheit = (celsius * (9/5)) + 32
conversaoKelvin = celsius + 273,15
print('A conversão ', conversaoFahrenheit) 
print(conversaoKelvin)  