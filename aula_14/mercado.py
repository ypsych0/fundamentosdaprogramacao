total = 0
quantidade = 0

while True:
    valor = float(input("Digite o valor do produto: "))
    
    if valor == 0:
        break
    
    total += valor
    quantidade += 1

if quantidade > 0:
    media = total / quantidade
    
    if total > 100:
        desconto = total * 0.10
        total_final = total - desconto
        print(f"\nDesconto de 10% aplicado: R$ {desconto:.2f}")
    else:
        total_final = total
    
    print(f"Total: {total_final:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhum produto foi comprado.")