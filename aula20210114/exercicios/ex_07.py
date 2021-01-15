
if __name__ == '__main__':
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    operacao = input("Digite a operação desejada: ")
    operacao = operacao.lower()
    resultado = None

    if operacao == "soma":
        resultado = numero1 + numero2

    elif operacao == "subtracao":
        resultado = numero1 - numero2

    elif operacao == "multiplicacao":
        resultado = numero1 * numero2

    elif operacao == "divisao":
        resultado = numero1 / numero2

    else:
        print("Operação não reconhecida.")

    print(resultado)