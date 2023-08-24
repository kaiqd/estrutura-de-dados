def somarDigitos(n):

    if n < 10:
        return n

    return n % 10 + somarDigitos(n // 10)

print(somarDigitos(1234))