# Exercício Python #017 - Catetos e Hipotenusa
#
# https://youtu.be/vmPW9iWsYkY?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
#  Faça um programa que leia o comprimento do cateto oposto
#  e do cateto adjacente de um triângulo retângulo.
#  Calcule e mostre o comprimento da hipotenusa.

a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('Digite o comprimento do cateto adjacente: '))

print(f"\nO comprimento da hipotenusa é {((a**2)+(b**2))**0.5}.")