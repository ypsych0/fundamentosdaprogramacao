idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Matrícula NEGADA")
else:
    nota = float(input("Digite sua nota: "))
    frequencia_escolar = float(input("Informe sua Frequência escolar (%): "))

if nota >= 9:
    print("Aluno APROVADO")

elif idade >= 18 and nota >= 6 and frequencia_escolar >= 75:
    print("Matrícula APROVADA")
else:
    print("Matrícula NEGADA")