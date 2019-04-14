# Python 3.7
# Vinícius Augusto 
import os,math

def LimpaTela():
    os.system("cls" if os.name == "nt" else "clear")

LimpaTela()

print("""
 ######     ###    ##        ######  ##     ## ##          ###    ########   #######  ########     ###    
##    ##   ## ##   ##       ##    ## ##     ## ##         ## ##   ##     ## ##     ## ##     ##   ## ##   
##        ##   ##  ##       ##       ##     ## ##        ##   ##  ##     ## ##     ## ##     ##  ##   ##  
##       ##     ## ##       ##       ##     ## ##       ##     ## ##     ## ##     ## ########  ##     ## 
##       ######### ##       ##       ##     ## ##       ######### ##     ## ##     ## ##   ##   ######### 
##    ## ##     ## ##       ##    ## ##     ## ##       ##     ## ##     ## ##     ## ##    ##  ##     ## 
 ######  ##     ## ########  ######   #######  ######## ##     ## ########   #######  ##     ## ##     ##
"""
)
print("""
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Bhaskara
6 - Sair do programa
""")

try:
    opcao = int(input("Escolha uma opção: "))

except KeyboardInterrupt:
    print("Fim do programa!")
except ValueError:
    print("Opção incorreta!!!")

try:
    if opcao == int(1):
        n1 = float(input("Número 01: "))
        n2 = float(input("Número 02: "))
        somar = (n1 + n2)
        print("N1= {}\nN2= {}\nResultado = {}".format(n1,n2,somar))
        input("")

    elif opcao == int(2):
        n1 = float(input("Número 01: "))
        n2 = float(input("Número 02: "))
        subtrair = (n1 - n2)
        print("N1= {}\nN2= {}\nResultado = {}".format(n1,n2,subtrair))
        input("")
    elif opcao == int(3):
        n1 = float(input("Número 01: "))
        n2 = float(input("Número 02: "))
        multiplicar = (n1 * n2)
        print("N1= {}\nN2= {}\nResultado = {}".format(n1,n2,multiplicar))
        input("")
    elif opcao == int(4): #Filtrar os erros
        n1 = float(input("Número 01: "))
        n2 = float(input("Número 02: "))
        
        if n1 == int(0):
            print("Resultado = 0")
            input("")
        elif n2 == int(0):
            print("Não é possível dividir por zero!")
            input("")
        else:
            dividir = (n1 + n2)
            print("N1= {}\nN2= {}\nResultado = {}".format(n1,n2,dividir))
            input("")

    elif opcao == int(5): #Filtrar os erros
        a = float(input("Valor de A: "))
        b = float(input("Valor de B: "))
        c = float(input("Valor de C: "))

        delta = b ** 2 - 4 * a * c

        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Δ = b² - 4ac")
        print("Δ = {}".format(round(delta),1))
        print("")
        print("X = -b +- √Δ / 2a")
        print("")
        print("X¹ = {}".format(round(x1),1))  
        print("X² = {}".format(round(x2),1))
        input("")

    elif opcao == int(6):
        print("Fim do programa!")
        input("")
    else:
        pass


except KeyboardInterrupt:
    print("Fim do programa!")
    input("")
except ValueError:
    print("Error!")
    input("")
except ZeroDivisionError:
    print("Divisão por zero!!")
    input("")
