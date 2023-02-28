Numero_escolhido = int(input('Escolha um numero para verificar se pertence a sequência de Fibonacci: '))

def fibonacci(num):
    """
    Função que retorna a sequência de Fibonacci
    """
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    return fib


def verifica_fibonacci(num):
    """
    Função que verifica se um determinado número pertence à sequência de Fibonacci.
    """
    fib = fibonacci(num)
    if num in fib:
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")


# Verificação
verifica_fibonacci(Numero_escolhido)
