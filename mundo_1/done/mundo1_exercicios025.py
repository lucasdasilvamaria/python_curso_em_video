# Exercício Python #025 - Procurando uma string dentro de outra
#
# https://youtu.be/WHWGz2Dy1ZU
#
# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.

# Lê o nome completo do usuário, remove espaços extras, coloca em minúsculas
# e separa em uma lista de palavras
nome = input('Digite seu nome completo: ').strip().lower().split()

# Passo a passo:

# 1. input() → lê o nome digitado pelo usuário.
# 2. .strip() → remove espaços extras no início e no fim da string.
#    Ex: "   João da Silva   " vira "João da Silva"

# 3. .lower() → transforma todas as letras em minúsculas, garantindo que
#    "Silva", "SILVA" ou "silva" sejam tratados igual.

# 4. .split() → separa o nome em palavras individuais, criando uma lista.
#    Ex: "João da Silva" vira ['joão', 'da', 'silva']

# Verifica se a palavra "silva" está presente na lista de palavras
if 'silva' in nome:
    print('Tem "SILVA" no nome.')  # Se estiver, imprime que o nome tem "SILVA"
else:
    print('Não tem "SILVA" no nome.')  # Caso contrário, imprime que não tem

# Explicação do funcionamento:
# - A lista 'nome' contém todas as palavras do nome do usuário.
# - O operador 'in' verifica se a palavra exata "silva" aparece na lista.
#   Isso evita falsos positivos como "Silvana".
# - Com isso, qualquer cidade ou pessoa que tenha "Silva" como palavra completa
#   será detectada corretamente.