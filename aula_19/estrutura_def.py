# As funçôes podem ou não receber propriedades
def saudacao():
    print("Olá, seja bem-vindo!")

# Invocação da função
# saudacao()

# Calcule o preço total de uma pizza onde será passado um dicionário com os tamanhos e valores. Além disso, o cliente pode solicitar ou não a borda recheada. Ao final, retorne o preço
# 1.Pequena, Média ou Grande. Qualquer pizza terá o mesmo valor dependendo do tamanho
# 2.Se o cliente optar pela borda recheada, deverá acrescido no valor da pizza mais +R$8

def calcular_preco_pizza(tamanho, borda_recheada=False):
    "Calcula o preço final de uma pizza com opções"
    tabela = {"P": 25.0, "M": 35.0, "G": 45.0}
    preco = tabela[tamanho]
    if borda_recheada:
        preco += 8.0
    return preco

print(calcular_preco_pizza("P"))
print(calcular_preco_pizza("P", True))
print(calcular_preco_pizza("M"))
print(calcular_preco_pizza("M", True))
print(calcular_preco_pizza("G"))
print(calcular_preco_pizza("G", True))