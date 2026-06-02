# Parâmetros nomeados - Ao nomear os argumentos, a ordem não importa mais.

def registrar_cliente(nome, telefone, endereco):
    print(" === DADOS DO CLIENTE ===")
    print(f"Cliente registrado: {nome}")
    print(f"Telefone: {telefone}")
    print(f"Endereço: {endereco}")

# registrar_cliente(nome="João", telefone="123456789", endereco="Rua A, 123")

# Retorno de valores - desempacotamento de retorno (unpacking) - Devolve uma tupla com os returns

def resumo_pedido(itens, desconto=0):
    subtotal = sum(itens)
    valor_desconto = subtotal * (desconto / 100)
    total = subtotal - valor_desconto
    return subtotal, valor_desconto, total # Devolve uma tupla (subtotal, valor_desconto, total)

# Invocando e desempacotando a função/retorno
# resumo_pedido([35.0, 12.0, 8.5], 10)
sub, desc, tot = resumo_pedido([35.0, 12.0, 8.5], desconto=10)
print(f" Subtotal: R$ {sub:.2f}")
print(f" Desconto: R$ {desc:.2f}")   
print(f" Total: R$ {tot:.2f}")                