
if __name__ == '__main__':
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media < 5:
        print("Você está reprovado.")
        
    elif media >= 5 and media < 7:
        print("Você está de recuperação.")

    else:
        print("Você está aprovado")