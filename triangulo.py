# Calculo que indicara se o triângulo é escaleno, isóceles ou equilatero
def triangulo():
    escaleno = "Escaleno"
    equilatero = "Equilatero"
    isoceles = "Isóceles"
    l1 = int(input(">> Digite o valor do primeiro lado do triângulo: "))
    l2 = int(input(">> Digite o valor do segundo lado do triângulo: "))
    l3 = int(input(">> Digite o valor do terceiro lado do triângulo: "))
    if l1 + l2 > l3 or l2 + l3 > l1 or l1 + l3 > l2:
        if l1 == l2 and l2 == l3 and l3 == l1:
            print(f"Esse triângulo é o: {equilatero}")
        elif l1 == l2 and l2 != l3 or l2 == l3 and l3 != l1 or l3 == l1 and l1 != l2:
            print(f"Esse triângulo é o: {isoceles}")
        elif l1 + l2 and l2 != l3 or l3 != l1:
            print(f"Esse triângulo é o: {escaleno}")
        else:
            print("Coloque valores válidos")
triangulo()