#Calculo de quanto um fumante gastou com cigarro até o momento
def cigarro():
    tempo = float(input(">> A quantos anos você fuma: "))
    totcigarros = int(input("Quantos cigarros você fuma por dia: "))
    valmaco = float(input("Qual o valor do maço de cigarro: "))
    valcigarros = valmaco * 20
    anos = tempo * 365
    y = float(anos * totcigarros * valcigarros)
    print(y)
cigarro()