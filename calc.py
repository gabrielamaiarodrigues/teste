def calc(a, b):
    if a == b: return "a igual b"
    else:
        if a > b:
            res = a - b
            print("a é maior")
        else:
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
