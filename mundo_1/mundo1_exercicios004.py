# Desafio 4
# Exercício Python #004 - Dissecando uma Variável
# Crie um script Python que leia qualquer input do teclado e diga o seu tipo primitivo
# e todas as informações possíveis sobre ele.

a = input('Digite qualquer coisa: ')
# Lê um valor do teclado. Tudo que vem de input() é do tipo str (string).

print('O tipo primitivo desse valor é:', type(a))
# Mostra o tipo do valor armazenado em 'a'. Aqui será sempre <class 'str'>,
# a não ser que façamos conversão para int ou float manualmente.

print('Só tem espaços?',  "Sim." if a.isspace() else "Não.")
# Verifica se a string contém apenas espaços em branco.

print('É alfabético?',  "Sim." if a.isalpha() else "Não.")
# Verifica se a string contém apenas letras (sem números ou símbolos).

print('É numérico (digitos)?',  "Sim." if a.isdigit() else "Não.")
# Verifica se a string contém apenas dígitos (0–9).

print('É numérico (decimal)?',  "Sim." if a.isdecimal() else "Não.")
# Verifica se a string contém apenas caracteres decimais (mais restrito que isnumeric).

print('É numérico (numérico em geral)?',  "Sim." if a.isnumeric() else "Não.")
# Verifica se a string contém apenas caracteres numéricos
# (inclui números em outros alfabetos, frações, expoentes, etc).

print('É alfanumérico?',  "Sim." if a.isalnum() else "Não.")
# Verifica se a string contém apenas letras e/ou números (sem espaços ou símbolos).

print('É identificador válido em Python?',  "Sim." if a.isidentifier() else "Não.")
# Verifica se o texto digitado pode ser usado como nome de variável em Python
# (não pode começar com número, nem ter espaço, nem caracteres inválidos).

print('Está em maiúsculas?',  "Sim." if a.isupper() else "Não.")
# Verifica se todas as letras da string estão em maiúsculas.

print('Está em minúsculas?',  "Sim." if a.islower() else "Não.")
# Verifica se todas as letras da string estão em minúsculas.

print('Está capitalizado?',  "Sim." if a.istitle() else "Não.")
# Verifica se a string está no formato "title case" (primeira letra maiúscula em cada palavra).

print('É imprimível?',  "Sim." if a.isprintable() else "Não.")
# Verifica se todos os caracteres da string são imprimíveis (ou seja, que podem aparecer na tela).
