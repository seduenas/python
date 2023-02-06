"""operaciones_de_calculadora"""
#funcion de sumatoria
def sumar(lista_sumandos):
    suma_final= 0
    for sumando in lista_sumandos:
        suma_final+=int(sumando)
    return str(suma_final)

#Funcion de resta
def restar(minuendo):
    return minuendo[0]-minuendo[1]

#Funcion de multiplcacion
def multiplicar(lista_multiplicados):
    multiplicacion_final=1
    for multiplicado in lista_multiplicados:
        multiplicacion_final*=multiplicado
    return multiplicacion_final

#Funcion de division
def dividir(divisor):
    return divisor[0]/divisor[1]

#Funcion de numero factorial
def factorial(base):
    resultado=1
    for i in range(1,base+1):
        resultado *= i
    return resultado

#Funcion de exponente
def exponencial(exponentes):
    return exponentes[0]**exponentes[1]

#Funcion de concatenado de strings
def operacion_texto(string,operador):
    operacion=""
    for char in string:
        operacion+= str(char) + str(operador)
    return operacion[:-1]