turma = []

quantidade = int(input("Quantas aulos serão cadastrados?: "))

for i in range(quantidade):
    print(f"\nCadastro do {i+1} aluno")

    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a 1° nota"))
    nota2 = float(input("Digite a 2° nota"))
    nota3 = float(input("Digite a 3° nota"))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Essa linha guarda todas as informações do aluno dentro da lista turma. 
    # Tive que pesquisar essa parte pois o senhor não mostrou isso para gente.
    turma.append([nome, nota1, nota2, nota3, media, situacao])

print("\nBOLETIM DA TURMA")

for aluno in turma:
    print(f"nome: {aluno[0]}")
    print(f"Notas: {aluno[1]}, {aluno[2]}, {aluno[3]}")
    # Tive alguns problemas quando a média retornava em dízima periódica, então fui pesquisar na web alguma forma de deixar o número em decimal e encontrei.
    # .1f Ele mostra 1 casa decimal. (Eu também posso colocar .2f, que ele mostra 2 casas decimais, e assim por diante.) O f significa número do tipo float e é usado para formatar número decimal dentro do f-string.
    print(f"Média: {aluno[4]:.1f}")
    print(f"Situação: {aluno[5]}")
    
