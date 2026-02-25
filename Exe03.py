'''
3. Desenvolva um programa para calcular e escrever a área e o perímetro de um retângulo.
Exemplo: 
Base= 5
Altura = 4
Área = 20
Perímetro = 18
'''

#ENTRADA
base = float(input('Informe a base do retângulo: '))
altura = float(input('Informe a altura do retângulo: '))

#base, altura = map(float, input('Informe base e a altura: ').split())

#Processamento
area = base * altura
perimetro = (base * 2) + (altura * 2)

#SAIDA
print('Área do retângulo:', area)
print('Perímetro do retângulo:', perimetro)