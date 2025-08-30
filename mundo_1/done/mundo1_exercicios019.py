# Exercício Python #019 - Sorteando um Item na Lista
#
# https://youtu.be/_Nk02-mfB5I?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#  Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo
#  na tela o nome do escolhido.

from random import choice
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print(f"\nO escolhido foi {escolhido}.")