
if __name__ == '__main__':
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))

    if numero1 < numero2 and numero1 < numero3:
        print(f"O menor número é {numero1}")

    elif numero2 < numero1 and numero2 < numero3:
        print(f"O menor número é {numero2}")

    elif numero3 < numero1 and numero3 < numero2:
        print(f"O menor número é {numero3}")

    else:
        print("Os números são iguais")

    # Dá pra fazer a mesma coisa utilizando a função built-in min()
    # menor_numero = min(
    #     [numero1, numero2, numero3]
    # )
    #
    # print(menor_numero)