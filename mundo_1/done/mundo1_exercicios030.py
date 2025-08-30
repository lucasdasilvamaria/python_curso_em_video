# Exercício Python #030 - Par ou Ímpar?
#
# https://youtu.be/4vFCzKuHOn4?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
# Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

# Solicita que o usuário digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

#% 2 retorna o resto da divisão do número por 2.
# Se o resto for 0, o número é par; caso contrário, é ímpar.
