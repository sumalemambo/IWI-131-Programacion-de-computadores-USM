################################################################
# Certamen 1 2019 Nombre: Ignacio Quintana ROL:201973610-8     #
# Mail: ignacio.quintana@usm.cl                                #
################################################################


def f1(st):
    c = 0
    h = len(st)
    s = 0
    while c < h:
        if c != h-1 and st[c+1] == '-':
            c += 2
        else:
            c += 3
        s += 1
    return s

def verificar_numero(numero,carton):
    lenght = f1(carton)
    h = len(carton)
    c = 0
    while(lenght != 0):
        if c != h-1:
            if(carton[c+1] == '-'):
                if(int(carton[c]) == numero):
                    return True
                c += 2
            else:
                num = int(carton[c]) * 10 + int(carton[c+1])
                if(num == numero):
                    return True
                c += 3
        else:
            if(int(carton[c]) == numero):
                return True
        lenght -= 1
    return False

carton1 = str(input("Ingrese carton del Jugador 1: "))
carton2 = str(input("Ingrese carton del Jugador 2: "))
c1_lenght = f1(carton1)
c2_lenght = f1(carton2)  #Esta linea puede resultar innecesaria si consideramos que ambos jugadores tendran cartones de misma longitud, de la misma forma si consideramos eso en el ciclo while el c2_lenght debera ser reemplazado por c1_lenght como el ejercicio no especifica lo dejo asi
c1 = 0
c2 = 0

while(c1 != c1_lenght and c2 != c2_lenght):
    numero = int(input("Ingrese numero de la tombola : "))
    if(verificar_numero(numero,carton1) == True):
        c1 += 1
    if(verificar_numero(numero,carton2) == True):
        c2 += 1
if(c1 == c2):
    print("Ambos jugadores ganan")
elif(c1 > c2):
    print("El ganador es el Jugador 1")
else:
    print("El ganador es el Jugador 2")
