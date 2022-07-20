#impares: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49
#pares: 2; 4; 6; 8; 10; 12; 14; 16; 18; 20; 22; 24; 26; 28; 30; 32; 34; 36; 38; 40; 42; 44; 46; 48; 50

#impares
quantidade_alunos = int(input("Digite a quantidade de alunos ímpares."))
nota_total = 0

for n_alunos_impares in range (1, quantidade_alunos + 1, 2):
    notas = float(input("Você está avaliando os alunos ímpares. Digite a nota do aluno de número {}".format(
    n_alunos_impares)))
    nota_total = nota_total + notas

media_impares = nota_total / quantidade_alunos
print("A média da turma de alunos ímpares é {}".format(nota_total, media_impares))

#pares
quantidade_alunos = int(input("Digite a quantidade de alunos pares."))
nota_total = 0

for n_alunos_impares in range (2, quantidade_alunos + 1, 2):
    notas = float(input("Você está avaliando os alunos pares. Digite a nota do aluno de número {}".format(
    n_alunos_impares)))
    nota_total = nota_total + notas

media_pares = nota_total / quantidade_alunos
print("A média da turma de alunos pares é {}".format(nota_total, media_pares))

if media_impares > media_pares:
    print("A maior média é dos alunos com número impar!")
else:
    media_pares > media_impares
    print("A maior média é dos alunos com número par!")