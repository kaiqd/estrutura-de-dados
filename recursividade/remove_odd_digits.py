def removeImpares(num):
    if num == 0:
        return 0
    else:
        digito = num % 10
        if digito % 2 != 0:
            return removeImpares(num // 10)
        else:
            return removeImpares(num // 10) * 10 + digito

# Exemplo de uso
numero = 123456789
resultado_impares = removeImpares(numero)

print("Nnmero original:", numero)
print("Resultado apos remover impares:", resultado_impares)