'''
2. Crie um programa que leia as quatro notas de um aluno e mostra na tela a sua média final.
Exemplo: 
N1 = 6,0
N2 = 7,5
N3 = 5,5
N4 = 10
Média = 7,25
'''

#ENTRADA
n1 = float(input('Informe a nota 01: '))
n2 = float(input('Informe a nota 02: '))
n3 = float(input('Informe a nota 03: '))
n4 = float(input('Informe a nota 04: '))

#n1, n2, n3, n4 = map(float, input('Informe as notas: ').split())

#PROCESSAMENTO
media = (n1 + n2 + n3 + n4) / 4

#SAIDA
print('Media final:', media)