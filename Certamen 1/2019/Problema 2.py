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
    if(A >= B and A >= C and A >= D and A >= 4):
        return 'A'
    elif(B >= A and B >= C and B >= D and B >= 4):
        return 'B'
    elif(C >= A and C >= B and C>= D and C >= 4):
        return 'C'
    elif(D >= A and D >= B and D >= C and D >= 4):
        return 'D'
    else:
        return ''
#Problema 2) b)
#######################################################################
# Programa principal                                                  #
# Descripcion: En cada iteracion pregunta un numero de 4 digitos      #
# correspondiente a los discos A,B,C y D ,y calcula cual es el mejor  #
# al final obtiene cual se repite como mejor                          #
#######################################################################
rep = 1000
A = B = C = D = 0
while(rep != 0):
    string = mejor(int(input())) 
    if(string == 'A'):
        A += 1
    elif(string == 'B'):
        B += 1
    elif(string == 'C'):
        C += 1
    elif(string == 'D'):
        D += 1
    rep-=1


if(A >= B and A >= C and A >= D):
    max = 'A'
    maxCant = A
elif(B >= A and B >= C and B >= D):
    max = 'B'
    maxCant = B
elif(C >= A and C >= B and C>= D):
    max = 'C'
    maxCant =  C
else:
    max = 'D'
    maxCant = D

print("La mejor cancion fue " + max + " con " + str(maxCant) +" votos")
