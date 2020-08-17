################################################################
# Certamen 1 2017-1 Nombre: Ignacio Quintana ROL:201973610-8   #
# Mail: ignacio.quintana@usm.cl                                #
################################################################

#Problema 3 a)
def ganador(c1,c2,c3,meta):
    if(c1 < meta and c2 < meta and c3 < meta):
        return 0
    winner = 0
    if(c1 > c2 and c1 > c3):
        winner = 1
    if(c2 > c1 and c2 > c3):
        winner = 2
    if(c3 > c1 and c3 > c2):
        winner = 3
    return winner
#Problema 3b)
def contar(palabra):
    palabra = palabra.lower()
    vocales = 'aeiou'
    contador = 0
    for i in palabra:
        if i in vocales:
            contador += 1
    return contador
#Problema 3c)
def juego(meta):
    alianza1 = alianza2 = alianza3 = 0
    winner = 0
    while(winner == 0):
        al1 = contar(str(input("alianza 1: ")))
        al2 = contar(str(input("alianza 2: ")))
        al3 = contar(str(input("alianza 3: ")))

        if(al1 > al2 and al1 > al3):
            alianza1 += 1
        elif(al2 > al1 and al2 > al3):
            alianza3 += 1
        elif(al3 > al1 and al3 > al2):
            alianza2 += 1

        winner = ganador(alianza1,alianza2,alianza3,meta)
    print("La alianza ganadora es: "+ str(winner))

juego(int(input("Ingrese meta del juego: ")))
