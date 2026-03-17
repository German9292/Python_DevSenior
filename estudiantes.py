def registrar_estudiante():
    nombre = input('ingresa el nombre: ')

    edad = int(input('ingrese la edad; '))

    while edad <= 0:
        print('ERROR, INGRESE DE NUEVO LA EDAD')
        edad = int(input('ingrese la edad; '))

    nota1 = float(input('ingrese la primera nota: '))

    while nota1 < 0 or nota1 > 5:
        print('ERROR, INGRESE DE NUEVO LA NOTA')
        nota1 = float(input('ingrese la primera nota: '))

    nota2 = float(input('ingrese la segunda nota: '))

    while nota2 < 0 or nota2 > 5:
        print('ERROR, INGRESE DE NUEVO LA NOTA')
        nota2 = float(input('ingrese la segunda nota: '))

    nota3 = float(input('ingrese la tercera nota: '))

    while nota3 < 0 or nota3 > 5:
        print('ERROR, INGRESE DE NUEVO LA NOTA')
        nota3 = float(input('ingrese la tercera nota: '))

    return nombre, edad, nota1, nota2, nota3

def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

def confirmar_estado(promedio):
    if promedio >= 4.0:
        return 'APROBÓ'
    elif promedio >= 3.0:
        return 'RECUPERACIÓN'
    else:
        return 'REPROBÓ'

total_estudiante = 0
nota_promedio = 0

while True:
    print('--SISTEMAS DE ESTUDIANTES--')
    print('1. Registrar estudiante')
    print('2. Salir')

    opcion = input('Ingrese una opción: ')

    if opcion == '1':

        nombre, edad, nota1, nota2, nota3 = registrar_estudiante()
        total_estudiante += 1
        promedio = calcular_promedio(nota1, nota2, nota3)
        nota_promedio += promedio
        estado = confirmar_estado(promedio)
    
        print('El promedio es: ', promedio)
        print('El estado del estudiante es: ', estado)
    elif opcion == '2':
        break
print('El total de estudiantes registrados es: ', total_estudiante)

if total_estudiante > 0:
    promedio_general = nota_promedio / total_estudiante
    print('El promedio general es: ', promedio_general)