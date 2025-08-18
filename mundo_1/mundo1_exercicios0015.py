# Exercício Python #15 - Conversor de Temperaturas
#
# https://youtu.be/9l_Gay8BuAw
#
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = float(input('O carro percorreu quantos quilômetros? '))
t = float(input('Por quantos dias o carro foi alugado? '))

print(f"\nO valor do aluguel do carro é de R$ {((t*60)+(d*0.15)):.2f}.")