# Exercício Python #023 - Separando dígitos de um número
#
# https://youtu.be/wD2aerLMBWA?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
# Programa que lê um número de 0 a 9999 e mostra cada dígito separadamente

num = int(input('Digite um número de 0 a 9999: '))
# 1️⃣ Lemos o número digitado pelo usuário com input()
# 2️⃣ Convertendo para inteiro com int() para podermos fazer operações matemáticas
# Exemplo: se o usuário digitar 1834, num = 1834

# Agora vamos separar cada dígito usando divisão inteira (//) e módulo (%)

unidade = num // 1 % 10
# Unidade → o dígito mais à direita
# Passo 1: num // 1 → 1834 // 1 = 1834  (não altera o número)
# Passo 2: % 10 → 1834 % 10 = 4  (o resto da divisão por 10 é o último dígito)
# Resultado: unidade = 4

dezena = num // 10 % 10
# Dezena → o segundo dígito da direita
# Passo 1: num // 10 → 1834 // 10 = 183  (desloca os dígitos uma casa para a direita)
# Passo 2: % 10 → 183 % 10 = 3  (pega o último dígito do novo número)
# Resultado: dezena = 3

centena = num // 100 % 10
# Centena → o terceiro dígito da direita
# Passo 1: num // 100 → 1834 // 100 = 18  (desloca os dígitos duas casas para a direita)
# Passo 2: % 10 → 18 % 10 = 8  (pega o último dígito do novo número)
# Resultado: centena = 8

milhar = num // 1000 % 10
# Milhar → o quarto dígito da direita
# Passo 1: num // 1000 → 1834 // 1000 = 1  (desloca os dígitos três casas para a direita)
# Passo 2: % 10 → 1 % 10 = 1  (pega o último dígito do novo número)
# Resultado: milhar = 1

# Por fim, mostramos cada dígito separadamente
print(f'\nUnidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')

# ✅ Resumo visual do que acontece com 1834:
# Número original:   1   8   3   4
# Milhar (num//1000 %10) → 1
# Centena (num//100 %10) → 8
# Dezena (num//10 %10) → 3
# Unidade (num//1 %10) → 4

# Explicação rápida para memorizar:
# - "//" → divide e descarta o resto, desloca os dígitos para a direita
# - "%" → resto da divisão por 10, pega o último dígito
# Combinar "//" e "%" permite "dissecar" cada dígito de um número

# Obviamente, feito e comentado pelo Gepetão.
