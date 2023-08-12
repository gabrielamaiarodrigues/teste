def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def potencia(a, b):
    return a ** b

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

print("Calculadora Expandida")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Potência")
print("6. Fatorial")
print("7. Sequência Fibonacci")

opcao = int(input("Escolha uma operação (1/2/3/4/5/6/7): "))

if opcao in [1, 2, 3, 4, 5]:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
else:
    num = int(input("Digite um número: "))

if opcao == 1:
    print("Resultado:", soma(num1, num2))
elif opcao == 2:
    print("Resultado:", subtracao(num1, num2))
elif opcao == 3:
    print("Resultado:", multiplicacao(num1, num2))
elif opcao == 4:
    print("Resultado:", divisao(num1, num2))
elif opcao == 5:
    print("Resultado:", potencia(num1, num2))
elif opcao == 6:
    print("Resultado:", fatorial(num))
elif opcao == 7:
    print("Resultado:", fibonacci(num))
else:
    print("Opção inválida")
