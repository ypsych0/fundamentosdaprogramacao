idade = int(input("Imforme sua idade: "))
cadastro_shopping = input("Você possui um cadastro no nosso shopping? (s/n): ") == "s"
tipo_veiculo = input("Qual o tamanho do deu veículo? (Pequeno/Grande): ")
vip = input("Você possui nosso plano VIP (s/n): ") == "s"

if idade < 18:
    print("Entrada NEGADA você é menor de idade")
elif vip:
    print("Entrada liberada (VIP)")
elif tipo_veiculo == "grande":
    print("Entrada NEGADA veículo excedeu as normas de tamanho")
elif not cadastro_shopping:
    print("Entrada negada você não possui um cadastro")
else:
    print("Entrada Liberada, Volte sempre!!!")  
    




