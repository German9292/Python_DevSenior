# No recibe nada no devuelve nada
"""
def suma1():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")

suma1()
"""
# Recibe parametros pero no devuelve nada
"""
def suma2(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
suma2(n1, n2)
"""

# No recibe parametros pero devuelve un valor
"""
def suma3():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    resultado = n1 + n2
    return resultado

print(suma3())
"""

#recibe parámetros y devuelve un valor
def suma4(a,b):
    resultado = a + b
    return resultado

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
print(suma4(n1, n2))