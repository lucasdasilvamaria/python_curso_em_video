# Exercício Python #008 - Conversor de Medidas
#
# https://youtu.be/KjcdG05EAZc?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6#
#
# Faça um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

m = float(input('Comprimento em metros: '))
print(f"\n{m:.2f} m são {m*100:.0f} cm e {m*1000:.0f} mm.")
# Esta formatação dentro do f-string mostra com 2 casas decimais
# para metros e valores inteiros para cm e mm.