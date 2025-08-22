# Exercício Python #028 - Jogo da Adivinhação v.1.0
#
# https://youtu.be/kchC5KLZSZ4?si=sL-0FA2HItFshB9G
#
# Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

while True:
    print("\n")
    print("===" * 20)
    print("Vou pensar num número de 0 a 5. Tente adivinhar!")
    print("===" * 20)
    sleep(3)  # pause for 3 seconds
    computador = randint(0, 4)
    jogador = int(input('\nDigita aí, cara! Em que número eu pensei? '))
    sleep(3)  # pause for 3 seconds
    if computador == jogador:
        print(f"\nVocê acertou, seu zé da manga!\nEu tinha pensado em {computador}!")
    else:
        print(f"\nVocê se ferrou, haha! Eu tinha pensado em {computador}!")

    repetir = input("\nFala aí, tchê! Quer jogar de novo ou não? (sim/não) ").strip().lower()
    if repetir != 'sim':
        print('\nTchau, perdedor!')
        break