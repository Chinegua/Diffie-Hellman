
def in_alpha():
	w = input("------Introduzca alpha: ")
	w = w.split(',')
	return w

def in_module():
	w = input("------Introduzca el modulo: ")
	w = w.split(',')
	return w

def in_xb():
	w = input("------Introduzca xB: ")
	w = w.split(',')
	return w

def in_xa():
	w = input("------Introduzca xA: ")
	w = w.split(',')
	return w

def calculo(alfa,xa,xb,modulo):
    ya = (alfa ** xa)%modulo
    yb = (alfa ** xb)%modulo
    k1 = (yb ** xa)%modulo
    k2 = (ya ** xb)%modulo
    print(k1)
    print(k2)

    if(k1 == k2):
        print ("p = "+str(modulo)+", a = "+str(alfa)+", xa = "+str(xa)+", xb = "+str(xb)+", ya = "+str(ya)+", yb = "+str(yb)+", k = "+str(k1))
    else:
        print("No son iguales")


calculo(4,5,2,13);
