# Exercício Python #031 - Custo da viagem
#
# https://youtu.be/PGqHyzWoagc?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

# Pede a distância da viagem e guarda na memória.
print('\n')
print(('-')*(35))
dist = float(input('Digite a distância da viagem em km.\n\n(Para quilometragens quebradas,\nuse pontos em vez de vírgula.)\n\nDigite aqui: '))
print(('-')*(35))

tax_men_200 = 0.5 #taxa para distâncias menores do que 200km
valor_men_200 = tax_men_200 * dist #valor total para distâncias menores do que 200km
tax_mai_200 = 0.45 #taxa para distâncias maiores do que 200km
valor_mai_200 = tax_mai_200 * dist #valor total para distâncias maiores do que 200km

# Se a distância for >200km:
if dist > 200:
    print(f'Distância maior do que 200 km. Será cobrada uma taxa de R$ {tax_mai_200} por km.\nValor total: R$ {valor_mai_200}.')

# Se a distância for menor ou igual a 200km:
else:
    print(f'Distância menor ou igual a 200 km.\nSerá cobrada uma taxa de R$ {tax_men_200} por km.\n\nValor total: R$ {valor_men_200}')