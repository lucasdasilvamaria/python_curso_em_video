# Exercício Python #024 - Verificando as primeiras letras de um texto
#
# https://youtu.be/QroT8cZMRnc?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO"

cidade = input('Em que cidade você nasceu? ').strip().lower()

# Verifica se começa com "santo" sozinho ou seguido de espaço
if cidade == 'santo' or cidade.startswith('santo '):
    print('A cidade começa com "SANTO".')
else:
    print('A cidade NÃO começa com "SANTO".')

