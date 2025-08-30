# Exercício Python #032 - Ano bissexto
#
# https://youtu.be/cyGY_83m4Xw?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#
# Sá para saber se um ano é bissexto apenas pelo número dele,
# usando regras matemáticas. A regra é esta:
#
# 1. Se o ano for divisível por 4, ele PODE ser bissexto.
# 2. Se o ano for divisível por 100, ele não é bissexto,
# a menos que também seja divisível por 400.
#
# Ou seja:
#
# Exemplo 1: 2024 → divisível por 4, não é múltiplo de 100 → bissexto.
# Exemplo 2: 1900 → divisível por 4 e por 100, mas não por 400 → não é bissexto.
# Exemplo 3: 2000 → divisível por 4, por 100 e por 400 → bissexto.
#
# ------------------------------------------------------------------------------------
# Loop infinito para garantir que o usuário só saia quando digitar um valor válido
while True:
    # Pede para o usuário digitar um ano
    ano_input = input("Digite um ano: ")

    try:
        # Tenta converter a entrada do usuário para inteiro
        ano = int(ano_input)

        # Aqui aplicamos a regra do ano bissexto:
        # 1. Se o ano é divisível por 4 e não é divisível por 100 → bissexto
        # 2. Ou se o ano é divisível por 400 → bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"{ano} é bissexto!")  # Mostra que é bissexto
        else:
            print(f"{ano} não é bissexto.")  # Mostra que não é bissexto

        break  # Sai do loop, porque o usuário digitou um número válido

    except ValueError:
        # Se a conversão para inteiro falhar, cai aqui
        # Informa ao usuário que ele não digitou um número inteiro
        # O loop continua, pedindo novamente
        print("Você não digitou um número inteiro válido. Tente novamente.\n")
