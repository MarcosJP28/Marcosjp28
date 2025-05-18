def separando_numeros(numeros):
    total_pares = 0
    total_impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            print("Número par:", numero)
            total_pares += 1
        else:
            print("Número ímpar:", numero)
            total_impares += 1

    print("Total de números pares:", total_pares)
    print("Total de números ímpares:", total_impares)


numeros = [2, 7, 20, 13, 8, 5, 3, 12]
separando_numeros(numeros)
