verificar = True

while verificar == True:
    n = int(input('ingrese un numero entero positivo:'))

    if n > 0 :

        for i in range(1,11):
             print(n,"por", i, "es igual a:" , n*i)

        verificar - False
    else:
        print('el numero ingresado no es correcto.intentolo nuevamente.')