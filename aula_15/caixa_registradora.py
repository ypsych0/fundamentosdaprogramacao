total = 0
quantidade = 0

while True:
    preco = float(input("Digite o preço do produto (aperte 0 para encerrar): "))

    if preco == 0:
        break
    
    total += preco
    quantidade += 1

print("\nResumo da compra:")
print("Quantidade de produtos:", quantidade)
print("Valor total da compra: R$", total)