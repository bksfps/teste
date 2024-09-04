#EX 2
#Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def verificao(string):
    qnt_a_min = string.count('a')
    qnt_a_mais = string.count('A')

    if qnt_a_min > 0 or qnt_a_mais > 0:
        print(f"A letra 'a' minúscula aparece {qnt_a_min} vezes na string.")
        print(f"A letra 'A' maiúscula aparece {qnt_a_mais} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

entrada = input("Digite uma string: ")

verificao(entrada)
