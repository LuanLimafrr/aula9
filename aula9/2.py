#2.	Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []

for i in range (10):
    n = int(input(f'Digite o {i+1}º número da lista: '))
    numeros.append(n)
    #lista.reverse() vira a lista ao contrário


print(list(reversed(numeros)))
        #também vira a lista ao contrário, porém mais objetivo
    
