#Calculo de volume
def volume():
    r = float(input(">> Digite o valor do raio:" ))
    a = float(input(">> Digite o valor da altura: "))
    volume = (3.14 * r**2 * a)
    print(f"O valor é: {volume}")
volume()