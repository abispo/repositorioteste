# Laço While

if __name__ == '__main__':
    lista_de_numeros = []
    continuar = True
    contador = 0

    while contador < 10:
        valor = input("Digite um número (ou 'SAIR' para sair): ")

        if valor.upper() == "SAIR":
            break

        lista_de_numeros.append(int(valor))
        contador += 1

    print(lista_de_numeros)