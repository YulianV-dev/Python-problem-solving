# -*- coding: utf-8 -*-
"""
#Tema 1: 

#Metros a centimetros

metros = float(input("Metros: "))
centimetros = metros * 100
print("Centímetros:", centimetros)


#Celsius a Fahrenheit

c = float(input("Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)


#Area de triangulo

base = float(input("Base: "))
altura = float(input("Altura: "))
area = (base * altura) / 2
print("Área:", area)

#Tema 2:

#Si es multiplo de 5

n = int(input("Número: "))
if n % 5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo de 5")
    

#Si el estudiante reprobo

nota = float(input("Nota: "))
if nota >= 3:
    print("Aprobado")
else:
    print("Reprobado")


#Positivo o negativo

n = float(input("Número: "))
if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Cero")
    
    
#Tema 3:
    
#Dia de la semana
    
dia = int(input("Número del 1 al 7: "))

match dia:
case 1: print("Lunes")
case 2: print("Martes")
case 3: print("Miércoles")
case 4: print("Jueves")
case 5: print("Viernes")
case 6: print("Sábado")
case 7: print("Domingo")
case _: print("Número inválido")


#Perimetro area de un circulo

op = input("Operación (a=area, p=perímetro): ")

match op:
case "a":
lado = float(input("Lado: "))
print("Área:", lado * lado)
case "p":
lado = float(input("Lado: "))
print("Perímetro:", lado * 4)
case _:
print("Opción no válida")


#Tipo de usuario

tipo = int(input("1=Invitado, 2=Usuario, 3=Admin: "))

match tipo:
case 1: print("Acceso limitado")
case 2: print("Acceso estándar")
case 3: print("Acceso total")
case _: print("No existe ese tipo de usuario")
    

#Suma de rangos

suma = 0
for i in range(1, 21):
suma += i
print("Suma:", suma)


#Cantidad de numeros pares ingresados 10 numeritos

pares = 0
for i in range(10):
n = int(input("Número: "))
if n % 2 == 0:
pares += 1

print("Cantidad de pares:", pares)


#Promedio de notas

suma = 0
for i in range(8):
nota = float(input(f"Nota {i+1}: "))
suma += nota

print("Promedio:", suma / 8)


#
"""