def fahrenheit_para_celsius(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c
    
temp_f = 75
temp_c = fahrenheit_para_celsius(temp_f)
print(temp_f, "graus Fahrenheit equivalem a", temp_c, "graus Celsius.")
temp_c_arredondado = round(temp_c, 1)
print(temp_f, "graus Fahrenheit equivalem a", temp_c_arredondado, "graus Celsius.")