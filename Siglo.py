Pase=1
while(Pase==1):
    Siglo=input("Ingrese un a�o :")
    print""
    print""
    if(Siglo%100==0):
        S=Siglo/100
        print "El Siglo de a�o %s " % Siglo,"es %d " % S
        print""
        Pase=input("Quiere ingresar otro a�o digite 1 para si 0 para no: ")
        print""
    
    else:
        S=Siglo/100+1
        print "El Siglo de a�o %s " % Siglo,"es %d " % S
        print""
        Pase=input("Quiere ingresar otro a�o digite 1 para si 0 para no: ")
        print""
    
    
