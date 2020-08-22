################################################################
# Certamen 1 2019 Nombre: Ignacio Quintana ROL:201973610-8     #
# Mail: ignacio.quintana@usm.cl                                #
################################################################

##################################################################
# Funcion: mejor                                                 #
# Input: un numero entero de 4 digitos, con digitos del 1 al 7   #
# Descripcion: obtiene la cancion con mejor calificacion         #
##################################################################

#Problema 2) a)

def mejor(votos):

    D = votos % 10
    votos = votos // 10
    C = votos % 10
    votos = votos // 10
    B = votos % 10
    votos = votos // 10
    A = votos % 10
    votos = votos // 10

    if(A < 4 and B < 4 and C < 4 and D < 4):
        return ''
    elif(A > B and A > C and A > D):
        return 'A'
    elif(B > A and B > C and B > D):
        return 'B'
    elif(C > A and C > B and C > D):
        return 'C'
    else:
        return 'D'
#Problema 2) b)
#######################################################################
# Programa principal                                                  #
# Descripcion: En cada iteracion pregunta un numero de 4 digitos      #
# correspondiente a los discos A,B,C y D ,y calcula cual es el mejor  #
# al final obtiene cual se repite como mejor                          #
#######################################################################
A = B = C = D = 0
for i in range(0,1000):

    a = mejor(int(input("Voto? ")))

    if(a == 'A'):
        A += 1
    elif(a == 'B'):
        B += 1
    elif(a == 'C'):
        C += 1
    elif(a == 'D'):
        D += 1

if(A > B and A > C and A > D):
    a = 'A'
    maximo = A
elif(B > A and B > C and B > D):
    a = 'B'
    maximo = B
elif(C > A and C > B and C > D):
    a  = 'C'
    maximo = C
else:
    a = 'D'
    maximo = D

print("El ganador fue " + a + " con " + str(maximo) + " votos")
