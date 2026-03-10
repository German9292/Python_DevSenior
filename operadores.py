"""edad1 = 25
edad2 = 30
nombre1 = 'juan'
nombre2 = 'maria'

print(f'la edad de {nombre1} es {edad1} y la edad de {nombre2} es {edad2}')

a,b,c = 1,2,3
print(f'los valosres son a={a}, b={b}, c={c}')

n1 = n2 = n3 = 5

print(f'los valores son n1={n1}, n2{n2}, n3{n3}')"""


#numero1 = 7
#numero2 = 3

#print(f'la suma de los numeros es: {numero1+numero2} la resta de los nuemros es: {numero1-numero2}, la multiplicacion es: {numero1*numero2}, la divicion es: {numero1/numero2} la divicion entera es: {numero1//numero2}, el modulo es {numero1%numero2} y la portencia es {numero1**numero2}')
"""print(f'la suma de los numeros es: {numero1+numero2}')
print(f'la resta de los nuemros es: {numero1-numero2}')
print(f'la multiplicacion es: {numero1*numero2}')
print(f'la divicion es: {numero1/numero2}')
print(f'la divicion entera es: {numero1//numero2}')
print(f'el modulo es {numero1%numero2}')
print(f'y la portencia es {numero1**numero2}')"""


"""radio = float(input('ingrese el valor del radio '))
area = 3.1416 * radio **2

print('el valor del radio es:', f'{area:.2f}')"""

"""base = float(input('ingrese el valor de la base '))
altura = float(input('ingrese el valor de la altura '))

area = (base * altura) / 2

print(f'el area del triangulo es: {area}')"""



"""valor_hora = int(input('Ingrese el valor de la hora: '))
Empleado1_horas = int(input('ingrese la cantidad de hora empleado 1: '))
Empleado2_horas = int(input('ingrese la cantidad de hora empleado 2: '))
Empleado3_horas = int(input('ingrese la cantidad de hora empleado 3: '))

total_pagar = Empleado1_horas + Empleado2_horas + Empleado3_horas * valor_hora 

print('El valor a pagar es: ', f'{total_pagar:.0f}')"""

horas1 = float(input("Cuantas horas trabajo el empleado? "))
pago_por_hora1 = int(input("Cuanto gana por hora? "))
sueldo1 = horas1 * pago_por_hora1

horas2 = float(input("Cuantas horas trabajo el empleado? "))
pago_por_hora2 = int(input("Cuanto gana por hora? "))
sueldo2 = horas2 * pago_por_hora2

horas3 = float(input("Cuantas horas trabajo el empleado? "))
pago_por_hora3 = int(input("Cuanto gana por hora? "))
sueldo3 = horas3 * pago_por_hora3

nomina = sueldo1 + sueldo2 + sueldo3
print("El valor a pagar a los empleados por su trabajo de la semana es: ", nomina)
      