def removePares(num):
    if num == 0:
        return 0
    else:
        digito = num % 10
        if digito % 2 == 0:
            return removePares(num // 10)
        else:
            return removePares(num // 10) * 10 + digito

print(removePares(123456789))