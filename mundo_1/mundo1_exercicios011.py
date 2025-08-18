# Exercício Python #011 - Pintando Paredes
#
# https://youtu.be/mzSJpn9ldt4?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6
#
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

a = float(input('Digite a altura da parede (metros): '))
l = float(input('Digite a largura da parede (metros): '))
print(f"\nA área da parede é de {a*l:.2f} metros quadrados.\nCada litro de tinta pinta 2.00 metros quadrados.\nEntão você vai precisar de {(a*l)/2} litros de tinta.")