# Crie um sistema aonde o valor inicial é de R$ 1.000 e o usuário consiga realizar um saque e ao final seja exibido o valor restante do saldo.
saldo = 1000
while saldo > 0:
    saque = float(input("Digite o valor de saque: "))
    saldo -= saque #saldo = saldo - saque
    print(f'Saldo restante: {saldo}')
