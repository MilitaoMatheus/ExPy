#Calculo de parcela
def parcela():
    v = float(input(">> Digite o valor da parcela:"))
    t = float(input(">> Digite o valor da taxa:"))
    ta = float(input(">> Digite o valor do tempo em atraso:"))
    p = v + (v * t) / 100 * ta
    print(f"O resultado é: {p}")
parcela()