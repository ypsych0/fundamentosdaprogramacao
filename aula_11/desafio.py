idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Empréstimo negado, você é menor de idade.")
else:
    salario = float(input("Digite seu salário: "))
    tempo_trabalho = int(input("Digite seu tempo de trabalho (em anos): "))

if salario >= 5000:
    print("Empréstimo aprovado.")

elif idade >= 18 and salario >= 2000 and tempo_trabalho >= 2:

    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")




