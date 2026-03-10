"""sueldo = int(input('ingrese el sueldo del empleado: '))
if sueldo < 2000000:
    print('si se cumplió la condición')
    sueldo += 200000
else:
    print('no se cumplió')
print('el sueldo del empleado es: ', sueldo)"""

"""escribir un programa en py que le solicite al usuario la edad y determinar si es mayor de edad o no, si la edad es mayor o = a 18 es mayo si no es menor"""

"""edad = int(input('Ingrese la edad: '))

if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

print('La edad es: ', edad)"""

"""Escribir un programa en py que solicite un numero entre 1 y 7, si es 1 lunes, si es 2 martes,etc..."""

"""numero = int(input('Ingrese un número entre 1 y 7: '))

if numero == 1:
    print('Lunes')
elif numero == 2:
    print('Martes')
elif numero == 3:
    print('Miercoles')
elif numero == 4:
    print('Jueves')
elif numero == 5:
    print('Viernes')
elif numero == 6:
    print('Sabado')
elif numero == 7:
    print('Domingo')
else:
    print('Numero no valido')"""

"""
preguntar al usuario un animal (perro, gato, pez)
si el animal es perro imprimir "Guau"
si el animal es gato imprimir "Miau"    
si el animal es pez imprimir "Blub"
y si el animal no es ninguno de esos imprimir "Animal no reconocido"
"""

"""animal = input('Ingrese si el animal es Gato, Perro o Pez: ')

match animal:
    case 'gato':
        print('Miau')
    case 'perro':
        print('Guau')
    case 'pez':
        print('Blub')
    case _:
        print('Animal no valido')"""

tabla = int(input('ingrese que tabla de multiplicar desea: '))
i= 1

while i <= 10:
    print(tabla,'x', i ,'=',tabla * i)
    i +=1



