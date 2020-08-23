################################################################
# Certamen 1 2019 Nombre: Ignacio Quintana ROL:201973610-8     #
# Mail: ignacio.quintana@usm.cl                                #
################################################################

def byte(numero,lenght):
    contador = 0
    num = 0
    for i in range(lenght,-1,-1):
        if numero[contador] != '0':
            if numero[contador] == '1':
                num += 2 ** i
            else:
                return -1
        contador += 1
    return num

t = 1
impar = 0
par = 0

while(t == 1):
    read = str(input("Ingrese cadena binaria: "))
    auxiliar = byte(read,len(read)-1)
    if(auxiliar != -1):
        if auxiliar % 2 == 0:
            par += 1
        else:
            impar += 1
    else:
        t = 0

print("total " + str(impar+par))
print("impares " + str(impar))
print("pares " + str(par))
