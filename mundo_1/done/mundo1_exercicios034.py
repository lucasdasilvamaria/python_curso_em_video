# Exercício Python #024 - Aumentos múltiplos
#
# https://www.youtube.com/watch?v=Sfadj_AzKHw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=35
#
# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o salário do funcionário: '))
if sal > 1250:
    print(f'O salário terá um aumento de 10%. O valor atualizado será de R$ {sal*1.1:.2f}.')
else:
    print(f'O salário terá um aumento de 15%. O valor atualizado será de R$ {sal * 1.15:.2f}.')