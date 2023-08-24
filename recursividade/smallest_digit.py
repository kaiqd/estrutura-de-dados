def menorDigito(n):

    if n < 10:
        return n

    ultimo_digito = n % 10
    menor_resto = menorDigito(n // 10)
    
    if ultimo_digito < menor_resto:
        return ultimo_digito
    else:
        return menor_resto

print(menorDigito(23147))