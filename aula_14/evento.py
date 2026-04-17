while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    convite = input("Você possui o convite? (s/n): ") == "s"

    if idade < 16:
        print("Entrada negada")
        
    elif not convite:
        print("Entrada negada, você não possui um convite")
    
    elif idade >= 16 and convite:
        print("Entrada liberada")
    else:
        print("Entrada negada")
    break

    


