nombre = input('ingrese nombre:')
salario = int(input('ingrese su salario:'))
edad = int(input('ingrese su edad:'))

if edad <= 16:
    print('no tiene edad para trabajar')

elif edad >19 and edad >=50:
        salario += (salario*0.05)
        print(f'el nuevo salario seria {salario}')


 
elif edad >51 and edad >=60:
    salario += (salario * 0.10)
    print (f'Su nuevo salrio seria {salario} ')
    

elif edad >60:
    salario += (salario * 0.15)
    print (f'Su nuevo salario seria {salario}')