# Exercício Python #14 - Conversor de Temperaturas
#
# https://youtu.be/9l_Gay8BuAw
#
# Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

s = float(input('Digite a temperatura em graus Celsius (°C): '))
print(f"\nA temperatura em graus Fahrenheit (°F) é igual a {((s*(9/5))+32):.2f} °F.")
print(f"A temperatura em graus Kelvin (°K) é igual a {s+273.15:.2f} °K.")