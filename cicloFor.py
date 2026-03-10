"""for x in range(1, 11):
    print(x)

texto = 'python'
for letra in texto:
    print(letra)
"""

tabla = int(input('Ingrese la tabla que desea: '))

for i in range(1, 11):
    resultado = tabla * i
    
    print(tabla, 'X', i, '=', resultado)