def contarDigitos(n):

    if n < 10:
        return 1


    return 1 + contarDigitos(n // 10)

print(contarDigitos(403))