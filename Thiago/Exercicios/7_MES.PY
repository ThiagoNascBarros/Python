'''
Descrição   : Escreva um algoritmo para exibir o nome do mês por extenso
                de acordo com o número que o representa:
                        1	    Janeiro
                        2	    Fevereiro
                        3	    Março
                        4	    Abril
                        5	    Maio
                        6	    Junho
                        7	    Julho
                        8	    Agosto
                        9	    Setembro
                        10	    Outubro
                        11	    Novembro
                        12	    Dezembro

'''
esc = 0
esc_escolha = ''
esc = int(input("Qual mês: "))

if(esc == 1):
    esc_escolha = "Janeiro"
elif(esc == 2):
    esc_escolha = "Fevereiro"
elif(esc == 3):
    esc_escolha = "Março"   
elif(esc == 4):
    esc_escolha = "Abril"
elif(esc == 5):
    esc_escolha = "Maio"
elif(esc == 6):
    esc_escolha = "Junho"
elif(esc == 7):
    esc_escolha = "Julho"
elif(esc == 8):
    esc_escolha = "Agosto"
elif(esc == 9):
    esc_escolha = "Setembro"
elif(esc == 10):
    esc_escolha = "Outubro"
elif(esc == 11):
    esc_escolha = "Novembro"
else:
    esc_escolha = "Dezembro"

print(esc_escolha)