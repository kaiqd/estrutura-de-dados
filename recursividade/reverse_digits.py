def inverteDigitos(number, reverse = 0):
    if number == 0:
        return reverse
    return inverteDigitos(number // 10, reverse * 10 + number % 10)

print(inverteDigitos(12345))