def calcular_media(lista_numeros):
    total = 0
    for i in range(len(lista_numeros)):
        total += lista_numeros[i]
    media = total / len(lista_numeros)
    return media

def verificar_paridade(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def main():
    quantidade_numeros = int(input("Digite a quantidade de números: "))
    numeros = []
    for i in range(quantidade_numeros):
        num = int(input("Digite o {}º número: ".format(i+1)))
        numeros.append(num)

    media = calcular_media(numeros)
    print("A média dos números é:", round(media, 2))

    num_verificar = int(input("Digite um número para verificar se é par: "))
    if verificar_paridade(num_verificar):
        print("O número é par.")
    else:
        print("O número é ímpar.")

if __name__ == "__main__":
    main()
