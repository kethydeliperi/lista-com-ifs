tempo = int(input("Digite os minutos que aparecem no relógio da sua máquina: "))

valor2 = 1

for tempo in range (1, tempo + 1):
    valor2 *= tempo

print("A senha é LIBERDADE{}.".format(valor2))