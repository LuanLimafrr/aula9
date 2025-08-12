#7.	Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista = []
soma = []
mult = []

for i in range(5):
    n = int(input(f'Digite o {i+1}º número inteiro: '))
lista.append(n)
soma2 = sum(n)
soma.append(soma2)
multiplica = (n*n)
mult.append(multiplica)


print(f'soma = {soma}, multiplicação = {mult}, números aplicados: {lista}')