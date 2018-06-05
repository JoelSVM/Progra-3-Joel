Pase=1
while(Pase==1):
    Siglo=input("Ingrese un año :")
    print""
    print""
    if(Siglo%100==0):
        S=Siglo/100
        print "El Siglo de año %s " % Siglo,"es %d " % S
        print""
        Pase=input("Quiere ingresar otro año digite 1 para si 0 para no: ")
        print""
    
    else:
        S=Siglo/100+1
        print "El Siglo de año %s " % Siglo,"es %d " % S
        print""
        Pase=input("Quiere ingresar otro año digite 1 para si 0 para no: ")
        print""
    
    
