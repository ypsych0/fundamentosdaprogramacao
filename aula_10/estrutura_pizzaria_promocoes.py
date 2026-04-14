# Variáveis da pizzaria 
FRETE = 2 #constante Fake
nome = input("Por favor, informe seu nome: ")
pizza_sabor = input("Informe o sabor da pizza - [Frango com Requeijão], [Calabresa], [Mussarela], [Banana com Chocolate]: ")
pizza_tamanho = input("Informe o tamanho da pizza - [Pequena], [Média], [Grande]: ")
dia_semana = input("Informe o dia da semana - [Quarta], [Quinta], [Sexta], [Sábado]: ")

print(f"O sabor escolhida da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}.")

# Promoções -> Estruturas condicionais.

# Comprando qualquer pizza de qualuqer tamanho, sábado, o refri é gratuito.
if dia_semana == "sabado":
    print(f"Pedido aceito com sucesso!")
    print(f"O Refri hoje é por conta da casa!.")
elif dia_semana == "domingo":
    print(f"Pedido aceito com sucesso!")
    print(f"O Frete e o Refri hoje é por conta da casa!.")
elif pizza_sabor == "calabresa" and pizza_tamanho == "media":
    print(f"Pedido aceito com sucesso!")
    print(f"O Frete hoje é por conta da casa!.")
     
# Comprando uma pizza de calabresa de tamanho médio, em qualquer dia, o frete é gratuito.

# Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.
