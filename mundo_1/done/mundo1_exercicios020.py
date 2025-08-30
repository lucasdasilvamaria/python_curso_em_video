# Exercício Python #020 - Sorteando uma ordem na lista
#
# https://youtu.be/OPh0nngbBSY?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
#  O mesmo professor do desafio 019 quer sortear
#  a ordem de apresentação de trabalhos dos alunos.
#  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print(f"\nA ordem de apresentação será {lista}.")