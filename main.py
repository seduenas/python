""""
Este es un programa que ayuda a realizar calculos simples
"""

import operaciones
import validaciones

validaciones.historial("Calc Software 1.0 History \n")

while True:

    #Presentacion de opciones
    print("Que tipo de operacion desea realizar?")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Numero Factorial")
    print("6) Exponentes")
    print("7) Cerrar Calculadora \n")


    #Seleccion de operacion
    tipo_operacion= validaciones.entrada("Digite el numero de la operacion a realizar \n")


    operacion=[]
    operacion.clear()
    result=""

    #region Operacion_Suma
    if tipo_operacion==1:
        print("Suma Seleccionada!")
        while True:
            sumando=validaciones.entrada("Digite un numero a sumar \n")
            if sumando=="":
                break
            operacion.append(sumando)
        result=f"{operaciones.operacion_texto(operacion,'+')}=  {operaciones.sumar(operacion)}"
        print(result)
        validaciones.historial(result)
    #endregion

    #region Operacion_Resta
    elif tipo_operacion==2:
        print("Resta Seleccionada!")
        while len(operacion)< 2:
            resta_valores=validaciones.entrada("Digite un numero a restar \n")
            operacion.append(resta_valores)
        result=(f"{operaciones.operacion_texto(operacion,'-')}=  {operaciones.restar(operacion)}")
        print(result)
        validaciones.historial(result)
    #endregion

    #region Operacion_Multiplicar
    elif tipo_operacion==3:
        print("Multiplicacion Seleccionada!")
        while True:
            multiplicador=validaciones.entrada("Digite un numero a multiplicar \n")
            if multiplicador=="":
                break
            operacion.append(multiplicador)
        result=(f"{operaciones.operacion_texto(operacion,'x')}=  {operaciones.multiplicar(operacion)}")
        print(result)
        validaciones.historial(result)

    #endregion

    #region Operacion_Dividir
    elif tipo_operacion==4:
        print("Division Seleccionada!")
        while len(operacion)< 2:
            division_valores=validaciones.entrada("Digite un numero a dividir \n")
            operacion.append(division_valores)
        result=(f"{operaciones.operacion_texto(operacion,'/')}=  {operaciones.dividir(operacion)}")
        print(result)
        validaciones.historial(result)

#endregion

    #region Operacion_Factorial
    elif tipo_operacion==5:
        print("Numero Factorial Seleccionado!")
        factor=validaciones.entrada("Digite el numero factorial")
        if factor < 0 :
            print("El numero es menor a 0")
        else:
            result=(f"{factor}!=  {operaciones.factorial(factor)} ")
            print(result)
            validaciones.historial(result)


#endregion

    #region Operacion_Exponente
    elif tipo_operacion==6:
        print("Exponentes Seleccionado!")
        while len(operacion)< 2:
            exponente_valores=validaciones.entrada("Digite la base y luego el exponente \n")
            operacion.append(exponente_valores)
        result=(f"{operaciones.operacion_texto(operacion,'^')}=  {operaciones.exponencial(operacion)}")
        print(result)
        validaciones.historial(result)


    #endregion

    else:
        print("Cerrando Calculadora!")
        break