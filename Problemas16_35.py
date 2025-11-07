# -*- coding: utf-8 -*-
"""
"""

#16. Problema
 
a = float(input("primer número: "))
b = float(input("segundo número: "))
if a == b:
    resultado = a - b
    print(f"son iguales, entonces resta: {resultado}")
else:
    resultado = a + b
    print(f"son diferentes, por lo que suma: {resultado}")

    
#17. Problema

mat = input('digite la materia: ')
nom = input('digite el nombre del estudiante: ')
n1 = float(input('digite la primera nota: '))
n2 = float(input('digite la segunda nota: '))
n3 = float(input('digite la tercera nota: '))
sum = n1 + n2 + n3 
resultado = sum / 3

if sum > 3.0:
    print(f'el estudiante {nom} perdio la materia {mat} con {resultado}')
elif sum <= 3.0:
    print(f'{id} el estudiante {nom} gano la materia {mat} con {resultado}')
    


#18. Problema

articulos = int(input('digite la cantidad de los articulos: '))
cantidad = int(input('digite el valor del articulo: '))
total = cantidad * articulos
total_pagar = total

if total >= 100000:
    descuento = total * 0.20
    total_pagar = total - descuento
    print('tiene un descuento del 20% y le queda en {total_pagar}')
else:
    print('el total de la compra es de {total}')


#19. Problema

articulos = int(input('digite la cantidad de los articulos: '))
cantidad = float(input('digite el valor del articulo: '))
total = cantidad * articulos

if total < 20000:
    descuento = total * 0.15
    total_pagar = total - descuento
    print(f'tiene un descuento del 15% y le queda en {total_pagar}')
elif total >= 20000:
    descuento = total * 0.35
    total_pagar = total - descuento
    print('tiene un descuento del 35% y le queda en {total_pagar}')
    

#20. Problema

n = int(input('digite un numero: '))
if n > 0 and n % 2 == 0:
  print("El numero es par")
else:
  print("El numero es impar")
    

#21. Problema

lunes = float(input('digite la temperatura del lunes: '))
martes = float(input('digite la temperatura del martes: '))
miercoles = float(input('digite la temperatura del miercoles: '))
jueves = float(input('digite la temperatura del jueves: '))
viernes = float(input('digite la temperatura del virnes: ')) 
sabado = float(input('digite la temperatura del sabado: '))
domingo = float(input('digite la temperatura del domingo: '))
dias = lunes + martes + miercoles + jueves + viernes + sabado + domingo
promedio = dias / 7
if promedio > 35:
    print(f'la temperatura fue de {promedio} que semana tan calurosa')
elif promedio >= 15 and promedio <= 35:
    print(f'la temperatura fue de {promedio} que clima tan delicioso')
elif promedio < 15:
    print(f'la temperatura fue de {promedio} grados que semana tan fría')
else:
    print('clima no valido')
    
    
#22. Problema

compra = float(input("valor de la compra: "))

if 10000 <= compra <= 20000:
    descuento = compra * 0.10
elif 20001 <= compra <= 50000:
    descuento = compra * 0.30
elif compra > 50000:
    descuento = compra * 0.50
else:
    descuento = 0
total = compra - descuento

print(f"Valor a pagar: ${total}")


#23. Problema

edad = int(input("edad del deportista: "))
estatura = float(input("estatura en cm: "))
peso = float(input("peso en kg: "))

if edad <= 18 and estatura > 180 and peso <= 80:
    print("es aceptado en el equipo.")
else:
    print("no cumple las condiciones y es rechazado.")
    
    
#24. Problema

letra = input("letra pa saber si es no es vocal o no: ").lower()

match letra:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print(f"La letra '{letra}' es una vocal.")
    case _:
        print(f"La letra '{letra}' NO es una vocal.")


#25. Problema

print("opción:")
print("1. distancia (X = V * T)")
print("2. tiempo (T = X / V)")
print("3. velocidad (V = X / T)")

opcion = int(input("opción (1-3): "))

match opcion:
    case 1:
        v = float(input("velocidad (m/s): "))
        t = float(input("tiempo (s): "))
        x = v * t
        print(f"distancia recorrida del coso es: {x} metros.")
    case 2:
        x = float(input("distancia (m): "))
        v = float(input("velocidad (m/s): "))
        t = x / v
        print(f"tiempo: {t} segundos.")
    case 3:
        x = float(input("distancia (m): "))
        t = float(input("tiempo (s): "))
        v = x / t
        print(f"velocidad: {v} m/s.")
    case _:
        print("Opción no válida pendejo.")
        
#26. Problema

num = int(input("número: "))

print("Seleccione la opción:")
print("1. positivo o negativo")
print("2. par o impar")

opcion = int(input("opción (1 o 2): "))

match opcion:
    case 1:
        if num > 0:
            print(f"{num} es POSITIVO.")
        elif num < 0:
            print(f"{num} es NEGATIVO.")
        else:
            print("es CERO.")
    case 2:
        if num % 2 == 0:
            print(f"{num} es PAR.")
        else:
            print(f"{num} es IMPAR.")
    case _:
        print("Opción no válida pendejo.")


#27. Problema

while True:
    print("\n" + "="*30)
    print("**MENÚ DE OPCIONES**")
    print("1. Pasa o no la materia?")
    print("2. Es mayor o menor de edad?")
    print("3. Salir")
    print("="*30)
    
    opcion = input("Seleccione una opción (1, 2 o 3): ")
    
    if opcion == '1':
        print("\n--- Opción 1: Pasa o no la materia ---")
        try:
            nota1 = float(input("Ingrese la nota 1: "))
            nota2 = float(input("Ingrese la nota 2: "))
            nota3 = float(input("Ingrese la nota 3: "))
            
            promedio = (nota1 + nota2 + nota3) / 3
            print(f"El promedio es: {promedio:.2f}")
            
            if promedio > 3.0:
                print("**¡PASA la materia!**")
            else:
                print("**NO PASA la materia.**")
                
        except ValueError:
            print("Error: Ingrese solo números válidos para las notas.")

    elif opcion == '2':
        print("\n--- Opción 2: Es mayor o menor de edad ---")
        try:
            año_actual = int(input("Ingrese el año actual (ej. 2024): "))
            año_nacimiento = int(input("Ingrese su año de nacimiento (ej. 1990): "))
            
            if año_nacimiento > año_actual:
                print("Error: El año de nacimiento no puede ser futuro.")
                continue 
            
            edad = año_actual - año_nacimiento
            print(f"Su edad es: {edad} años")
            
            if edad >= 18:
                print("**Usted es MAYOR de edad.**")
            else:
                print("**Usted es MENOR de edad.**")
                
        except ValueError:
            print("Error: Ingrese un año válido (número entero).")

    elif opcion == '3':
        print("\n¡Hasta pronto!")
        break

    else:
        print("\nOpción no válida. Por favor, ingrese 1, 2 o 3.")
   
        
#28. Problema

for n in range(0, 1001):
    print(n)


#29. Problema

for n in range(0, 201, 2):
    print(n)


#30. Problema

for n in range(201, 500, 2):
    print(n)


#31. Problema

mayores = 0
for i in range(1, 21):
    edad = int(input(f"edad del estudiante {i}: "))
    if edad >= 18:
        mayores += 1

print(f"estudiantes mayores de edad: {mayores}")


#32. Problema
hombres = 0
mujeres = 0

for i in range(1, 26):
    sexo = input(f"sexo del estudiante {i} escribir (M/F): ").strip().lower()
    if sexo == 'm':
        hombres += 1
    elif sexo == 'f':
        mujeres += 1
    else:
        print("'no especificado'.")

print(f"Hombres: {hombres}")
print(f"Mujeres: {mujeres}")


#33. Problema

suma = 0.0
for i in range(1, 16):
    edad = float(input(f"edad del estudiante {i}: "))
    suma += edad

promedio = suma / 15
print(f"promedio: {promedio:.2f} años")


#34. Problema

suma = 0.0
for i in range(1, 19):
    est = float(input(f"estatura (cm) del estudiante {i}: "))
    suma += est

promedio = suma / 18
print(f"promedio: {promedio:.2f} cm")

if promedio < 140:
    print("Estudiantes muy bajos como yo")
elif 140 <= promedio <= 170:
    print("Estudiantes de estatura normal para chambear")
else:
    print("Estudiantes muy altos como postes")


#35. Problema

for n in range(3, 100, 3):
    print(n)
