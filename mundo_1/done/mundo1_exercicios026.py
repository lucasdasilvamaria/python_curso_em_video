# Exercício Python #026 - Primeira e última ocorrência de uma string
#
# https://youtu.be/23UOVEetNPY?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
# Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez
#
#
frase = str(input('Digite uma frase:'))
num = frase.count('a')
pos = frase.find('a')
pos2 = frase.rfind('a')
print(f'A letra A aparece na frase {num} vezes.')
print(f'A primeira letra A aparece na posição {pos+1}.')
print(f'A última letra A aparece na posição {pos2+1}.')