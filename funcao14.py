#palidromo = palavra ou frase igual de frente para tras e vice e versa
def verificar_palidromo(texto):
    texto = texto.lower().replace(" ", " ")
    return texto == texto [::-1]

#texto{::-1} inverte o texto

texto = "Socorram-me, subi no ônibus em Marrocos"
if verificar_palidromo(texto):
    print(texto, "é um palídromo.")
else:
    print(texto, 'não é um palídromo.')