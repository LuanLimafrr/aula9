#3.	Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


lista = []

for i in range (4):
    n = float(input(f'Digite a {i+1}ª nota: '))
    lista.append(n)
media = sum(lista) / 4

for i in range(1):
    print(f'Suas notas são: {lista}, e sua média é {media}')