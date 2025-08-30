# Exercício Python #022 - Analisador de Textos
#
# https://youtu.be/EQQt-6QqXOs?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome1 = str(input('Digite seu primeiro nome: '))
nome2 = str(input('Digite seu sobrenome: '))
print(f'\n{nome1.upper()} {nome2.upper()}')
letras_nome1 = len(nome1.replace(' ', ''))
letras_nome2 = len(nome2.replace(' ', ''))
print(f"O primeiro nome tem {letras_nome1} letras, sem contar os espaços.")
print(f"O sobrenome tem {letras_nome2} letras, sem contar os espaços.")
print(f"O nome completo tem {letras_nome1 + letras_nome2} letras, sem contar os espaços.")