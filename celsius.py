#Conversão de celsius para fahrenheit
def fahrenheit():
    celsius = float(input(">> Digite a temperatura em celsius: "))
    f = (celsius * 9 / 5 ) + 32
    print(f"A temperatura {celsius}º em fahrenheit é de: {f}º")
fahrenheit()