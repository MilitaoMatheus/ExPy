#Cálculo de bhaskara
import math
def bhaskara():
    a = int(input(">> Digite o valor de A: "))
    b = int(input(">> Digite o valor de B: "))
    c = int(input(">> Digite o valor de C: "))
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta != 0:
            x1 = ((-b + math.sqrt(delta)) / 2 * a)
            x2 = ((-b - math.sqrt(delta)) / 2 * a)
            print(f"O valor da primeira raíz é: {x1}")
            print(f"O valor da segunda raíz é: {x2}")
        elif delta == 0:
            x1 = ((-b + math.sqrt(delta)) / 2 * a)
            print(f"O valor da raíz é: {x1}")
        else:
            print("Não foi possível calcular, pois delta é menor que 0")
    else:
        print("Não foi possível calcular, pois A é igual a 0")
bhaskara()