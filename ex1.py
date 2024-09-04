#EX 1
#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def fibonacci(n):
    sequenciaFib = [0, 1]
    while sequenciaFib [-1] < n:
        sequenciaFib.append(sequenciaFib[-1] + sequenciaFib[-2])
    return sequenciaFib

def pertenceFib (n):
    sequenciaFib = fibonacci(n)
    if n in sequenciaFib:
        return f"O número {n} pertence a sequência de Fibonacci."
    else:
        return f"O número {n} não pertence a sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = pertenceFib(numero)
print(resultado)
