'''
5. Codifique um programa que leia um número inteiro qualquer e 
   imprima o seu sucessor e seu antecessor. 
   A seguir, uma ilustração da entrada e da saída de uma execução 
   do programa.

Exemplo:
valor = 7
antecessor = 6
sucessor = 8
'''
#Entrada
valor = int(input('Informe um valor numerico inteiro: '))

#processamento
antecessor = valor - 1
sucessor = valor + 1

#saida
print('Valor:', valor)
print('Antecessor:', antecessor)
print('Sucessor:', sucessor)
