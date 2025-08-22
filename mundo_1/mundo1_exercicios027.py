# Exercício Python #027 - Primeiro e último nome de uma pessoa
#
# https://youtu.be/SifYYsXhLM8?si=xu1tDVdryzMMTUdx
#
#  Faça um programa que leia o nome completo de uma pessoa,
#  mostrando em seguida o primeiro e o último nome separadamente.
#
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.)
#
nome = str(input('Digite seu nome completo:')).strip().split()
pri = nome[0]
ult = nome[-1]
print(f'Seu primeiro nome é {pri}.')
print(f'Seu último nome é {ult}.')