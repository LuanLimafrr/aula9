#9.	Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

# Criar uma lista vazia para armazenar os números
A = []

# Ler 10 números inteiros
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    A.append(numero)

# Calcular a soma dos quadrados
soma_quadrados = 0
for num in A:
    soma_quadrados += num ** 2  # eleva ao quadrado e soma

# Mostrar o resultado
print(f"A soma dos quadrados dos elementos do vetor é: {soma_quadrados}")