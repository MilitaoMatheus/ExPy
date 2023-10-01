#Cálculo de imposto de renda
def imprenda():
    ra = float(input(">> Digite o valor do rendimento anual: "))
    vtinss = float(input(">> Digite o valor total do inss: "))
    dm = float(input(">> Digite o gasto com dispensas médicas: "))
    nd = int(input(">> Digite o número de dependentes na residência: "))
    deducoes = vtinss + dm + (nd * 1080)
    bc = ra - deducoes
    if bc <= 10800:
        print(f"O imposto a ser pago é de: {bc}")
    elif bc <= 21600:
        imp = bc * (15/100) - 1620
        print(f"O imposto a ser pago é de: {imp}")
    elif bc >= 21000:
        imp = bc * (25/100) - 3720
        print(f"O imposto a ser pago é de: {imp}")
imprenda()