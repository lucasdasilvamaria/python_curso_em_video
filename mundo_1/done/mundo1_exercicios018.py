# Exercício Python #018 - Seno, Cosseno e Tangente
#
# https://youtu.be/9GvsphwW26k?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
#  Faça um programa que leia um ângulo qualquer
#  e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
a = float(input('Digite o ângulo: '))

seno = (math.sin(math.radians(a)))
print(f"\nO ângulo de {a:.0f} tem o SENO de {seno:.2f}.")
cosseno = math.cos(math.radians(a))
print(f"O ângulo de {a:.0f} tem o COSSSENO de {cosseno:.2f}.")
tangente = math.tan(math.radians(a))
print(f"O ângulo de {a:.0f} tem a TANGENTE de {tangente:.2f}.")