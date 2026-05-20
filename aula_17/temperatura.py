
temperaturas = []

for i in range(24):
    temp = float(input(f"Digite a temperatura da hora {i + 1}: "))
    temperaturas.append(temp)

maior = max(temperaturas)
menor = min(temperaturas)


media = sum(temperaturas) / 24

if media < 15:
    classificacao = "Frio"
elif media <= 25:
    classificacao = "Agradável"
else:
    classificacao = "Quente"


acima30 = 0

for temp in temperaturas:
    if temp > 30:
        acima30 += 1

print("\n--- RELATÓRIO ---")
print("Temperatura máxima:", maior, "°C")
print("Temperatura mínima:", menor, "°C")
print("Média das temperaturas:", media, "°C")
print("Classificação do dia:", classificacao)
print("Horas acima de 30°C:", acima30)