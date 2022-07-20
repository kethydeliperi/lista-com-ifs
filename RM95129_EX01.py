basic = float(0.3)
silver = float(0.2)
gold = float(0.1)
platinum = float(0.05)

assinatura = input("Insira sua assinatura: basic, silver, gold ou platinum")
faturamento = float(input("Qual seu faturamento anual?"))

if assinatura == "basic":
    print("O valor do bônus a pagar é", float(faturamento * 0.3))

elif assinatura == "silver":
    print("O valor do bônus a pagar é", float(faturamento * 0.2))

elif assinatura == "gold":
    print("O valor do bônus a pagar é", float(faturamento * 0.1))

elif assinatura == "platinum":
    print("O valor do bônus a pagar é", float(faturamento * 0.05))