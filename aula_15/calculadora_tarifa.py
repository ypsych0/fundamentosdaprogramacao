consumo = float(input("Digite o consumo de kWh: "))

if consumo < 0:
    print("valor invalido")
else:
    if consumo <= 100:
        tarifa = 0.40
    elif consumo <= 200:
        tarifa = 0.60
    else:
        tarifa = 0.90

    total = consumo * tarifa
    
    print(f"Consumo informado: {consumo} kWh")
    print(f"Valor total a pagar: R$ {total:.1f}")
