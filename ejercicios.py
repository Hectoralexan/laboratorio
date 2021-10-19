verificar = True

while verificar == True:
    x= int(input('ingrese un numero entero positivo:'))

    if x > 0 :

        for i in range(1,11):
             print(x,"por", i, "es igual a:" , x*i)

        verificar - False
    else:
        print('el numero ingresado no es correcto.intentolo nuevamente.')
