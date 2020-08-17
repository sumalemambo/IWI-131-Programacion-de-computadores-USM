def lenght(numero):
    num_size = 0
    while(numero != 0):
        numero = numero // 10
        num_size += 1
    return num_size

def invert(numero):
    num_size = lenght(numero)
    number = 0
    while(numero != 0):
        number += (numero %10) * 10**(num_size - 1)
        numero = numero // 10
        num_size -= 1
    return number

def palindromico(numero,pasos):
    numero += invert(numero)
    if(numero == invert(numero)):
        print("Generado en " + str(pasos) + " pasos")
        print("Palidromo final: " +str(numero))
    else:
        print("Intermedio: " + str(numero))
        palindromico(numero,pasos + 1)

palindromico(int(input("Ingrese un numero palindromico: ")),1)
