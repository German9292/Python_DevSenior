'''🔹 Parte 1: Condicionales (if / elif / else)
🟢 Ejercicio 1: Número positivo o negativo

Pide un número al usuario y muestra si es:

positivo

negativo

o cero'''
'''
numero = int(input('Ingrese un número: '))

if numero < 0:
    print('EL NÚMERO ES NEGATIVO')
elif numero > 0:
    print('EL NÚMERO ES POSITIVO')
else:
    print('EL NÚMERO ES 0')

'''

'''🟢 Ejercicio 2: Mayor de edad

Pide la edad y muestra:

"Eres menor de edad" si es menor de 18

"Eres adulto" si tiene entre 18 y 64

"Adulto mayor" si tiene 65 o más'''

'''
edad = int(input('Ingrese la edad: '))

if edad < 18:
    print('Eres menor de edad')
elif edad >= 18 and edad < 65:
    print('Eres adulto')
else:
    print('Eres un adulto mayor')

'''

'''🟢 Ejercicio 3: Calculadora simple

Pide dos números y una operación (+, -, *, /) y muestra el resultado usando if/elif.'''

num1 = int(input('Ingresa el primer número: '))
num2 = int(input('Ingresa el segundo número: '))
operacion = input('Ingresa la operación que deseas (+, -, *, /): ')

if operacion == '+':
    print(num1 + num2)
elif operacion == '-':
    print(num1 - num2)
elif operacion == '*':
    print(num1 * num2)
elif operacion == '/':
    print(num1 / num2)
else:
    print('OPERADOR INVALIDO')