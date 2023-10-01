#Calculo de combustivel gasto em viagem
def combgasto():
    tempo = float(input(">> Digite o tempo gasto na viagem: "))
    velocidade = float(input(">> Digite a velocidade: "))
    kmpl = float(input(">> Digite a quantidade de km/litro:"))
    dis = (tempo * velocidade)
    lit = int(dis / kmpl)
    print(f"A quantidade de combustível gasto é de: {lit}")
combgasto()