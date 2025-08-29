# Exercício Python #03 - Maior e menor valores
#
# https://www.youtube.com/watch?v=a_8FbW5oH6I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=34
#
#  Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Lê três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Caso todos os números sejam iguais
if num1 == num2 == num3:
    print(f"Todos os números são iguais: {num1}")

# Caso dois números sejam iguais
elif num1 == num2 or num1 == num3 or num2 == num3:
    # Dois iguais e um diferente
    if num1 == num2:
        igual = num1
        diferente = num3
    elif num1 == num3:
        igual = num1
        diferente = num2
    else:  # num2 == num3
        igual = num2
        diferente = num1

    # Determina maior e menor
    if igual > diferente:
        print(f"O número {igual} aparece duas vezes e é o maior.")
        print(f"O número {diferente} é o menor.")
    elif igual < diferente:
        print(f"O número {igual} aparece duas vezes e é o menor.")
        print(f"O número {diferente} é o maior.")
    else:  # não deveria ocorrer, mas cobre segurança
        print(f"O número {igual} aparece duas vezes e é igual ao outro número.")

# Caso todos sejam diferentes
else:
    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    print(f"O maior número é {maior}.")
    print(f"O menor número é {menor}.")
