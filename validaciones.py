"""Validacion de entrada de usuario"""

#Validacion de entrada de numeros
def entrada(texto_entrada):
    while True:
        input_usuario= input(f"{texto_entrada} \n")
        if input_usuario == "":
            return input_usuario
        try:
            int_input= int(input_usuario)
            return int_input

        except ValueError:
            print("Este programa recibe unicamente numeros \n")
            continue

#Salva la operacion en texto plano
def historial(texto):
    history= open("CalcHistory.txt", "a",encoding="utf-8")
    history.write(f"{str(texto)} \n")
    history.close()