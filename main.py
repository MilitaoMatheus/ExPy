def media():
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    mediafinal = (nota1 + nota2 + nota3) / 3

    if mediafinal <= 4:
        print(f"Sua nota é:  {mediafinal}. Reprovado!")

    elif mediafinal >= 5 and mediafinal <= 7:
        print(f"Sua nota é:  {mediafinal}. Está de recuperação!")

    else:
        print(f"Sua nota é:  {mediafinal} Você está aprovado!")

media()
