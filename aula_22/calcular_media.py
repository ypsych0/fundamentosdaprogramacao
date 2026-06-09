def calcular_media(nota1: float, nota2: float, nota3: float):
    for nota in[nota1, nota2, nota3]:
        if nota < 0 or nota > 10:
            return -1.0
    return round((nota1 * 2 + nota2 * 3 + nota3 * 5) / 10, 1)

media = calcular_media(7.0, 8.0, 9.0)
print(f"Média: {media}")

media2 = calcular_media(5.0, 6.0, 4.0)
print(f"Média: {media2}")

invalida = calcular_media(5.0, 11.0, 8.0)
print(f"Média: {invalida}")