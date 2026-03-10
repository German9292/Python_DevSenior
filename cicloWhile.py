menu = """Restaurante el buen sabor

1. Hamburguesa - $20.000
2. Pizza - $15.000
3. Ensalada - $12.000
4. Perro caliente - $9.000
5. Sachipapa - $12.500
6. Salir
"""
print(menu)

opcion = 0
total = 0
total_Hamburguesa = 0
cantidadHamburguesas = 0
total_Pizza = 0
cantidadPizzas = 0
total_Ensalada = 0
cantidadEnsaladas = 0
total_PerroCaliente = 0
cantidadPerros = 0
total_Salchipapa = 0
cantidadSalchipapa = 0

while opcion != 6:
    opcion = int(input("Ingrese una opción del menú: "))
    if opcion == 1:
        print("Has elegido Hamburguesa")
        total += 20000
        total_Hamburguesa += 20000
        cantidadHamburguesas += 1
    elif opcion == 2:
        print("Has elegido Pizza")
        total += 15000
        total_Pizza +=15000
        cantidadPizzas +=1
    elif opcion == 3:
        print("Has elegido Ensalada")
        total += 12000
        total_Ensalada +=12000
        cantidadEnsaladas +=1
    elif opcion == 4:
        print("Has elegido Perro Caliente")
        total += 9000
        total_PerroCaliente +=9000
        cantidadPerros += 1
    elif opcion == 5:
        print("Has elegido Salchipapa")
        total += 12500
        total_Salchipapa += 12000
        cantidadSalchipapa += 1
    elif opcion == 6:
        print("Gracias por visitar el Restaurante el Buen Sabor, su total es ", total , "¡Hasta luego!")
        print('Hamburguesas', total_Hamburguesa,'Cantidad', cantidadHamburguesas)
        print('Ensaladas', total_Ensalada, 'Cantidad', cantidadEnsaladas)
        print('Perros', total_PerroCaliente, ' Cantidad', cantidadPerros)
        print('Pizzas', total_Pizza, 'Cantidad', cantidadPizzas)
        print('Salchipapa', total_Salchipapa, 'Cantidad', cantidadSalchipapa)
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
    print(menu)
