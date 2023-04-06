def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero/2) + 1):
        if numero % i == 0:
            return False
    return True

numero = 53
if verificar_primo(numero):
    print(numero, "é primo.")
else:
    print(numero, "não é primo.")
            