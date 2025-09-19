def ejer1():
    edad = int(input("Ingrese una edad"))

    if edad <18:
            print("Menor de edad.")
    elif edad <=64:
            print("Adulto")
    else:
            print("Adulto mayor")



def ejer2():
        an = int(input("Ingrese el año: "))

        if (an % 4 == 0 and an % 100 != 0) or an % 400 ==0 :
            print("Es un año bisiesto")
        else:
            print("No es  un año bisiesto")

        if an % 2 ==0:
                print("El año es par")
        else:
                print("El año es impar")

def ejer3():
    monto = float(input("Ingrese monto en sole: "))
    print("\n1. Dolares")
    print("2. Euros\n")
    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:print("Dolares: ", round((monto/3.75),2))
        case 2:print("Euros: ", round((monto/4.05),0))
        case _:print("Opción invalida")

import math
def ejer4():
    print("Bienvenidad año sistema de calculos de área\n")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Circulo\n")

    opcion = int(input("Ingrese una opción: "))
    match opcion:
        case 1:
            lado = int(input("Ingrese lado: "))
            print("Área del cuadrado: ", lado*lado)
        case 2:
            bs = int(input("Ingrese la base: "))
            altura = int(input("Ingrese la altura: "))
            print("Área deñ triangulo: ", bs*altura)
        case 3:
            bse = int(input("Ingrese la base: "))
            al = int(input("Ingrese la altura: "))
            print("Área del triangulo: ", (bse*al)/2)
        case 4:
            radio = float(input("Ingrese el radio: "))
            print("Área del circulo: ", round((math.pi * radio**2),2))
        case _: print("Opción invalida")

ejer4()