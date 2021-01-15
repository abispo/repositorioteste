
if __name__ == '__main__':
    lista_de_clientes = [
        "João", "Marcelo", "Rebecca", "Maria", "Lorena"
    ]

    if "Rebecca" in lista_de_clientes:
        print("Encontramos a Rebecca")

    for nome in lista_de_clientes:
        if nome == "Rebecca":
            print("Encontramos a Rebecca.")
            break
        else:
            continue
    else:
        print("Não encontramos a Rebecca")

    for nome in lista_de_clientes:
        for letra in nome:
            print(letra)
    