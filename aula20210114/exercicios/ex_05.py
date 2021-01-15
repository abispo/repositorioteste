
if __name__ == '__main__':
    nome_do_produto = input("Digite o nome do produto: ")
    valor_do_produto = float(input("Digite o valor do produto: "))
    desconto = 0.1

    if valor_do_produto >= 100:
        valor_do_produto = valor_do_produto - (valor_do_produto * desconto)

    print(f"O produto '{nome_do_produto}' custará {valor_do_produto}")