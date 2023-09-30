#conversão de fahrenheit para celsius
def celsius():
    fahrenheit = float(input(">>Digite o valor da temperatura em fahrenheit:"))
    celsius = (fahrenheit - 32 * 5) / 9
    print(f"O valor da tempertura em celsius é: {celsius}")
celsius()