#8.	Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.



alt = []

idades = []

for i in range(5):
    altura = float(input(f'Digite a altura da {i+1}ª pessoa: '))
    alt.append(altura)
    idade = int(input(f'Digite a idade da {i+1}ª pessoa: '))
    idades.append(idade)
alt.reverse()
idades.reverse()

print(f'idade das pessoas, da 5ª até a 1ª: {idades}\n Altura das pessoas, da 5ª até a 1ª: {alt}')