def calcular_raiz_quadrada(numero, precisao=0.0001):
    raiz = numero/2
    while abs(numero - raiz**2) > precisao:
        raiz = (raiz + numero/raiz)/2
    return raiz
    
numero = 25
raiz = calcular_raiz_quadrada(numero)
print("A raiz quadrada de", numero, "é", raiz)
#abs utilizado para mostrar o valor absoluto de um número 
#exemplo a seguir
print (abs(-5))