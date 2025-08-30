# Exercício Python #016 - Quebrando um número
#
# https://www.youtube.com/watch?v=-iSbDpl5Jhw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=17
#
# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.
#
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

d = float(input('Digite um valor: '))

print(f"\nO número {d} tem a parte inteira {d:.0f}.")