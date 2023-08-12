def calc(a, b):
    if a == b: return "a igual b"
    else:
        if a > b:
            res = a - b
            print("a é maior")
        else:def fatorial(numero): return 1 if numero <= 1 else numero * fatorial(numero-1)

def fibonacci(n): return [0] if n == 1 else [0, 1] if n == 2 else fibonacci(n-1).append(fibonacci(n-1)[-1] + fibonacci(n-1)[-2]) or fibonacci(n-1)

def operacao(opc, x, y): return x + y if opc == 1 else x - y if opc == 2 else x * y if opc == 3 else x / y if opc == 4 else "Operação inválida"

def menu():
    print("Calculadora")
    print("1. Soma")
    print("2. Subtracao")
    print("3. Multiplicacao")
    print("4. Divisao")
    print("5. Fatorial")
    print("6. Fibonacci")
    opc = int(input("Escolha uma operação (1/2/3/4/5/6): "))
    if opc in [1, 2, 3, 4]:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        resultado = operacao(opc, num1, num2)
        print("Resultado:", resultado)
    elif opc in [5, 6]:
        num = int(input("Insira um número inteiro: "))
        resultado = fatorial(num) if opc == 5 else fibonacci(num)
        print("Resultado:", resultado)
    else:
        print("Operação inválida")

menu()

            res = b - a
            print("b é maior")
        return res

def fibonacci(n):
    if n <= 0: return []
    elif n == 1: return [0]
    elif n == 2: return [0, 1]
    else:
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib

a = int(input("Insira um número inteiro: "))
b = int(input("Insira outro número inteiro: "))

print("Resultado calc:", calc(a, b))
print("Resultado fibonacci:", fibonacci(b))
