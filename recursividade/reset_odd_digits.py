def zeraImpares(num):
    if num == 0:
        return 0
    else:
        digito = num % 10
        if digito % 2 != 0:
            digito = 0
        return zeraImpares(num // 10) * 10 + digito

numero = 458
numeroAlterado = zeraImpares(numero)
print("numero original:", numero, "\n" "numero apos a funcao:", numeroAlterado)