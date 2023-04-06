def funcao_detecta(n):
    if(n % 2 == 0):
        return 'É par'
    else:
        return "É ímpar"
        
print(funcao_detecta(int(input('Entre com um número: '))))