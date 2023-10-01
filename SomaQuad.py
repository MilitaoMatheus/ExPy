#Soma dos quadrados
def somaquad():
    num1 = float(input(">> Digite um número: "))
    num2 = float(input(">> Digite um número: "))
    num3 = float(input(">> Digite um número: "))
    num4 = float(input(">> Digite um número: "))
    result = ((num1 ** 2) + (num2 ** 2) + (num3 ** 2) + (num4 ** 2))

    print(f"A soma dos quadraddos desses números é de {result}")
somaquad()
