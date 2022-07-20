segunda_feira = input("Prefere segunda?")
terca_feira = input("Prefere terça?")
quarta_feira = input("Prefere quarta?")
quinta_feira = input("Prefere quinta?")
sexta_feira = input("Prefere sexta?")

segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

if segunda_feira == "sim":
    segunda = segunda + 1

elif terca_feira == "sim":
    terca = terca + 1

elif quarta_feira == "sim":
    quarta = quarta + 1

elif quinta_feira == "sim":
    quinta = quinta + 1

elif sexta_feira == "sim":
    sexta = sexta + 1

else:
    print("Dia inexistente")

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia escolhido para as lives foi segunda-feira")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O dia escolhido para as lives foi sexta-feira")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("O dia escolhido para as lives foi quarta-feira")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("O dia escolhido para as lives foi quinta-feira")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("O dia escolhido para as lives foi sexta-feira")

else:
    print("Empate, verificar com a coordenação.")