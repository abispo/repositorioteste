
if __name__ == '__main__':
    nome = input("Digite o seu nome: ")
    sobrenome = input("Digite o seu sobrenome: ")

    # lista = list(nome + ' ' + sobrenome)
    # lista.reverse()
    #
    # print(''.join(lista))

    # Também podemos usar o slice (fatiar) para inverter uma string
    texto = nome + ' ' + sobrenome
    print(texto[::-1])
