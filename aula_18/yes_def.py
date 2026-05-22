# Desenvolva um sistema de pizzaria onde será recebido o preço total, um desconto de 10%, e ao final exiba o valor total do pedido com esse desconto;

# Declarar uma def (função)
def calcular_total(nome, preco, desconto=0.10):
    valor_desconto = preco * desconto
    total = preco - valor_desconto
    return print(f""" Recibo
                 Pedido do cliente: {nome}
                 Valor do pedido: R$ {preco}
                 Desconto aplicado: {desconto}
                 Total: R$ {total:.2f}
                """)

#invocação da def
print(calcular_total("João", 45.90))
print(calcular_total("Ana", 38.50))
print(calcular_total("Pedro", 20.90))
print(calcular_total("Enzo", 77.30)) 
print(calcular_total("Bia", 60.80))
print(calcular_total("Julio", 15.70))                                                