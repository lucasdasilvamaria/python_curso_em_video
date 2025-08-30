# Exercício Python #029 - Radar eletrônico
#
# https://youtu.be/hgJ_ETNGSj8?si=n6cEKwV_xe9kMb08
#
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep
limit = 80
speed = int(input('\nDigite a velocidade do seu carro: '))
fine_factor = 17 # R$ por km acima do limite
fine = (speed-limit)*fine_factor
sleep(2)
print(f'\nSua velocidade foi de {speed} km/h.\nO limite de velocidade era de {limit} km/h.')
if speed > limit:
    print(f'Você deveria se envergonhar!\nA multa é de R$ {fine_factor},00 por quilômetro acima do limite.\nSua multa vai ser de R$ {fine},00.')
else:
    print('Tá de boas.')