'''6.Crie um programa que leia dois valores para as variáveis A e B,
   que efetue a troca dos valores de forma que a variável A passe 
   a ter o valor da variável B e que a variável B passe a ter o 
   valor da variável A. Apresente os valores trocados. 

Exemplo:
A=5
B=10

INVERTENDO

A=10
B=5
'''

#Entrada
valor_a = int(input('Informe o valor de A: '))
valor_b = int(input('Informe o valor de B: '))

#Saida
print('Valor de A:', valor_a)
print('Valor de B:', valor_b)

#Processamento
temp = valor_a #armazena temporariamente o valor de A para evitar perder esse dado
valor_a = valor_b
valor_b = temp

#Jeito python de fazer
#valor_a, valor_b = valor_b, valor_a

#Saida
print('***INVERTENDO***')
print('Valor de A:', valor_a)
print('Valor de B:', valor_b)