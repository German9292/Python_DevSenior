"""
Escriba un programa que pida al ususario 2 numeros y uestre un menu de opciones
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo
8. Salir
"""

operadores = """Escoja la operación

1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo
8. Salir
"""

print(operadores)

opcion = 0

while opcion != 8:
    opcion = int(input('Ingrese la operación que desea: '))
    n1 = int(input('Ingrese el primer numero: '))
    n2 = int(input('ingrese el segundo numero: '))
    if opcion == 1:
        resultado = n1 + n2
    elif opcion == 2:
        resultado = n1 - n2
    elif opcion == 3:
        resultado = n1 * n2
    elif opcion == 4:
        resultado = n1 / n2
    elif opcion == 5:
        resultado = n1 // n2
    elif opcion == 6:
        resultado = n1 ** n2
    elif opcion == 7:
        resultado = n1 % n2
    elif opcion == 8:
        print('El resultado de la operacion es: ', resultado)
        break
    else:
        print('fin de la operacion')
    print(operadores)
    
