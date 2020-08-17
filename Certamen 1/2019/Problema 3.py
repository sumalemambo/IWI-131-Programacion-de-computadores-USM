def lenght(numero):
    num_size = 0
    while(numero != 0):
        numero = numero // 10
        num_size += 1
    return num_size

def palindromo(numero):
    num_size = lenght(numero)
    number = 0
    while(numero != 0):
        number += (numero %10) * 10**(num_size - 1)
        numero = numero // 10
        num_size -= 1
    return number

def palindromico(numero,pasos):
    numero += palindromo(numero)
    if(numero == palindromo(numero)):
        print("Generado en " + str(pasos) + " pasos")
        print("Palindromo final: " +str(numero))
    else:
        print("Intermedio: " + str(numero))
        palindromico(numero,pasos + 1)

palindromico(int(input("Ingrese un numero palidromico: ")),1)
