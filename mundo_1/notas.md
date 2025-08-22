16/08/2025

# O que fiz hoje:

Mundo1_Ex001.py

# O que aprendi hoje:

---

## cd

Muda a pasta atual do terminal.

Define onde o Python procura arquivos.

Exemplo:

    cd mundo-01
    python Mundo1_Ex001.py

---

## F-strings (f"...")

Strings formatadas: coloca variáveis e expressões em {}.

Mais legível que .format() ou +.

Exemplo:

    name = input("Digite seu nome: ")
    print(f"Olá, {name}")

Permite cálculos, listas, dicionários, datas, porcentagens e cores no terminal.

---

## Comandos que vou usar sempre que quiser atualizar o GitHub:

## git status
    Mostra quais arquivos foram modificados, adicionados ou removidos.
    Útil para conferir antes de commitar.

## git add .
    Adiciona todos os arquivos modificados e novos.
    Se quiser adicionar só um arquivo específico:
        git add caminho/do/arquivo.py

## git commit -m "Descrição do que mudou"
    Cria um commit

## git push
    Envia todas as alterações do commit atual para o repositório remoto.
    Como já configurou a branch principal (main), não precisa especificar nada mais.

## Resumo:
    git status
    git add .
    git commit -m "Radar eletrônico"
    git push

---

## Definindo input como float

Para receber um input como float em Python, utilize a função float() dentro da função input().

A função input() recebe a entrada do usuário como uma string, e float() converte essa string em um número de ponto flutuante (float). 
    
    numero_float = float(input("Digite um número com ponto decimal: "))
    print(numero_float)