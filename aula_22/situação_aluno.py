def verificar_situacao_aluno(media: float, verificar_honra = True):
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Em Recuperação"
    else:
        situacao = "Reprovado"

    honra = "menção honrosa" if (verificar_honra and media >= 9.0) else "sem menção honrosa"
    return situacao, honra

sit, honra = verificar_situacao_aluno(9.2)
print(f"{sit} {honra}")

sit2, honra2 = verificar_situacao_aluno(6.1)
print(f"{sit2} {honra2}")

sit3, honra3 = verificar_situacao_aluno(3.8, verificar_honra=False)
print(f"{sit3} {honra3}")