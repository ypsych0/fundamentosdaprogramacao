senha_correta = "ads2025"
tentativas = 0

while tentativas < 3:

    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso concedido")
        break

    else:
        tentativas += 1
        restam = 3 - tentativas

        print(f"Senha incorreta. Restam {restam} tentativa(s).")

if tentativas == 3:
    print("Acesso bloqueado")