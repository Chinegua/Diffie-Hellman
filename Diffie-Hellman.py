
def in_alpha():
	w = input("------Introduzca alpha: ")

	return int(w)

def in_module():
	w = input("------Introduzca el modulo: ")

	return int(w)

def in_xb():
	w = input("------Introduzca xB: ")

	return int(w)

def in_xa():
	w = input("------Introduzca xA: ")

	return int(w)

def exponente(y,b,mod):
    x = 1
    while (b > 1):
        if( b%2 == 0):
            print (str(y)+" | "+str(b)+ " | "+str(x))
            y = (y ** 2)%mod
            b = b/2
            print("es par")


        if(b%2 == 1):
            print (str(y)+" | "+str(b)+ " | "+str(x))
            b -= 1
            x = (x * y)%mod
            print("es impar")

    return x






def calculo(alfa,xa,xb,modulo):

    ya = exponente(alfa,xa,modulo)
    yb = exponente(alfa,xb,modulo)
    k1 = exponente(yb,xa,modulo)
    k2 = exponente(ya, xb, modulo)


    if(k1 == k2):
        print ("p = "+str(modulo)+", a = "+str(alfa)+", xa = "+str(xa)+", xb = "+str(xb)+", ya = "+str(ya)+", yb = "+str(yb)+", k = "+str(k1))
    else:
        print("No son iguales")


#calculo(in_alpha(),in_xa(),in_xb(),in_module());

calculo(43,54,71,113);
