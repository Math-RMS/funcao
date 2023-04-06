def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero-1)

numero = 5
fatorial = calcular_fatorial(numero)
print("o fatorial de", numero, "é", fatorial)