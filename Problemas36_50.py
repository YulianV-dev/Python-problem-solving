# -*- coding: utf-8 -*-

#36. Problema

num = float(input("número para mostrar su tabla (hasta 10): "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#37. Problema

for n in range(5, 101, 5):
    print(n)


#38. Problema

suma = 0.0
for i in range(1, 16):
    nota = float(input(f"nota {i}: "))
    suma += nota

promedio = suma / 15
print(f"Promedio: {promedio:.2f}")

if promedio >= 4.0:
    print("Gana la materia")
else:
    print("No gana la materia.")


#39. Problema

base = float(input("base: "))
exponente = int(input("exponente (entero): "))

# Caso del que el exponente sea 0 porque sos pendejo
if exponente == 0:
    resultado = 1.0
else:
    negative = exponente < 0
    e = abs(exponente)
    resultado = 1.0
    i = 0
    while i < e:
        resultado *= base
        i += 1
    if negative:
        resultado = 1.0 / resultado

print(f"{base} elevado a {exponente} = {resultado}")


#40. Problema

N = int(input("Numerito (entero positivo): "))
suma = 0
i = 1

while i <= N:
    suma += i
    i += 1

print(f"La suma de los {N} primeros números naturales es: {suma}")


#41. Problema

N = int(input("¿Cuántos números va a ingresar? "))

if N <= 0:
    print("número positivo de elementos.")
else:
    i = 1
    numero = float(input(f"número {i}: "))
    mayor = numero
    menor = numero
    i = 2

    while i <= N:
        numero = float(input(f"número {i}: "))
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
        i += 1

    print(f"El mayor es: {mayor}")
    print(f"El menor es: {menor}")


#42. Problema

n = int(input("¿Cuántos números desea ingresar? "))
for i in range(n):
    num = float(input("número: "))
    print("Cubo:", num**3)
    print("Cuarta potencia:", num**4)
    print("Quinta potencia:", num**5)
    print()

#43. Problema

buscar = float(input("número a buscar: "))
n = int(input("¿Cuántos números ingresará? "))

contador = 0

for i in range(n):
    num = float(input("número: "))
    if num == buscar:
        contador += 1

print("El número", buscar, "aparece", contador, "veces.")


#44. Problema

n = int(input("¿Cuántas calificaciones ingresará? "))

suma = 0
mayor = 0

for i in range(n):
    nota = float(input("nota: "))
    suma += nota
    if nota > mayor:
        mayor = nota

promedio = suma / n

print("promedio:", promedio)
print("Nota mayor:", mayor)

if promedio >= 4.0:
    print("GANA la materia.")
else:
    print("PIERDE la materia por pendejo.")


#45. Problema

num = int(input("número para calcular su factorial: "))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print("El factorial de", num, "es:", factorial)


#46. Problema

n = int(input("¿Cuántos productos va a ingresar? "))
total = 0

for i in range(n):
    precio = float(input("precio del producto: "))
    total += precio

print("Total:", total)


#47. Problema

n = int(input("¿Cuántos estudiantes? "))
mayor = 0

for i in range(n):
    est = float(input("estatura en cm: "))
    if est > mayor:
        mayor = est

print("La mayor estatura es:", mayor, "cm")


#48. Problema

opcion = 0
a = b = 0

while opcion != 6:
    print("\n1. Ingresar 2 números")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Salir")

    opcion = int(input("opción: "))

    if opcion == 1:
        a = float(input("primer número: "))
        b = float(input("segundo número: "))
    elif opcion == 2:
        print("Suma:", a + b)
    elif opcion == 3:
        print("Resta:", a - b)
    elif opcion == 4:
        print("Multiplicación:", a * b)
    elif opcion == 5:
        if b != 0:
            print("División:", a / b)
        else:
            print("No se puede dividir entre 0 pendejo")


#49. Problema

opcion = 0

while opcion != 3:
    print("\n1. Factorial (for)")
    print("2. Potencia (while)")
    print("3. Salir")
    opcion = int(input("opción: "))

    if opcion == 1:
        n = int(input("Número para factorial: "))
        fac = 1
        for i in range(1, n+1):
            fac *= i
        print("Factorial:", fac)

    elif opcion == 2:
        base = float(input("Base: "))
        exp = int(input("Exponente: "))
        cont = 1
        pot = 1
        while cont <= exp:
            pot *= base
            cont += 1
        print("Potencia:", pot)


#50. Problema

opcion = 0

while opcion != 4:
    print("\n1. pares hasta 100")
    print("2. de 4 hasta 100 (while)")
    print("3. Tabla de multiplicar")
    print("4. Salir")
    opcion = int(input("opción: "))

    if opcion == 1:
        for i in range(0, 101, 2):
            print(i)

    elif opcion == 2:
        i = 0
        while i <= 100:
            print(i)
            i += 4

    elif opcion == 3:
        n = int(input("Número: "))
        for i in range(1, 11):
            print(n, "x", i, "=", n*i)


#51. Problema

edades = []

for i in range(10):
    edad = int(input("edad: "))
    edades.append(edad)

print(edades)


#52. Problema

nombres = []

for i in range(15):
    nombre = input("nombre: ")
    nombres.append(nombre)

print(nombres)


#53. Problema

valores = []
suma = 0

for i in range(12):
    num = float(input("Ingrese un número: "))
    suma += num

print("Suma total:", suma)


#54. Problema

vector = []
pos = neg = ceros = 0

for i in range(20):
    num = float(input("Número: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        ceros += 1

print("Positivos:", pos)
print("Negativos:", neg)
print("Ceros:", ceros)


#55. Problema

vector = []

for i in range(20):
    num = input("Ingrese un valor: ")
    vector.append(num)

while True:
    pos = int(input("¿Qué posición desea ver? (1-20, otro número para salir): "))
    if pos < 1 or pos > 20:
        break
    print("Valor:", vector[pos-1])

