idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
tempo_trabalho = int(input("Digite seu tempo de trabalho (em anos): "))

aprovado = False

if idade >= 18:
    if salario >= 2000:
        if tempo_trabalho >= 2:
            aprovado = True
if aprovado:
    print("Empréstimo aprovado.")

else: print("Empréstimo negado.")
