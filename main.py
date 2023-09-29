#Função de calcular a média final de um aluno
def media():
    #Declaração de variáveis para a formula
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a terceira nota: "))
    #Formula para o calculo da media final
    mediafinal = (nota1 + nota2 + nota3 + nota4) / 4

    #Estrutura de condição
    if mediafinal <= 4:
        #O 'f' é uma das maneiras de concatenação em python
        print(f"Sua nota é:  {mediafinal}. Reprovado!")

    elif mediafinal >= 5 and mediafinal <= 7:
        print(f"Sua nota é:  {mediafinal}. Está de recuperação!")

    else:
        print(f"Sua nota é:  {mediafinal} Você está aprovado!")

media()
