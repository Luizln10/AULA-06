preçoOriginal = float(input("Digite o preço original:"))
desconto = float(input("Digite o valor do desconto:"))
desconto = preçoOriginal * 0.01
preçoDesconto = preçoOriginal - (preçoOriginal * desconto)
print(f"Produto final é {preçoDesconto}")
