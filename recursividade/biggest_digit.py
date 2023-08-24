def maiorDigito(n):

    if n < 10:
        return n

    ultimo_digito = n % 10
    maior_resto = maiorDigito(n // 10)
    
    if ultimo_digito > maior_resto:
        return ultimo_digito
    else:
        return maior_resto

# Resolução sem variáveis. 
def semVariaveis(n):
    if n < 10:
        return n
    
    return max(n % 10, semVariaveis(n // 10))

print(semVariaveis(89))
print(maiorDigito(73))