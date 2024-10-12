#QUESTÃO 1
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def conferir(valor):
    if valor < 0:
        return False

    n = 0
    while True:
        fibonacci(n)
#o cálculo da sequência é realizado até encontrar o valor fornecido ou passar dele, o que significa que ele não faz parte
        if fibonacci(n) == valor:
            return True
        if fibonacci(n) > valor:
            return False
        n+=1

entrada = int(input('Digite um número: '))
if conferir(entrada):
    print(entrada, "está na sequência de Fibonacci")
else:
    print(entrada, "NÃO está na sequência de Fibonacci")


