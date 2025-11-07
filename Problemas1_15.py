# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#1. Problema

a = float(input("primer número: "))
b = float(input("segundo número: "))
suma = a + b
print(f" el resultado es {suma}")


#2. Problema

x = float(input("primer número: "))
y = float(input("segundo número: "))
z = float(input("tercer número: "))
resultado = x * y * z
print(f"el resultado es {resultado}")


#3. Problema

v = float(input("velocidad (m/s): "))
t = float(input("tiempo (s): "))
x = v * t
print(f"distancia recorrida del coso {x} unidades")


#4. Problema

fecha_actual = int(input("año actual (ej. 2025): "))
nac = int(input("año de nacimiento: "))
edad = fecha_actual - nac
print(f"Tiene {edad} años")


#5. Problema

n = float(input("número para calcular el porcentaje: "))
veinte_p = n * 0.20
print(f"El 20% de {n} es {veinte_p}")


#6. Problema

num = float(input("número pa sacar porcentajes: "))
p30 = num * 0.30
p60 = num * 0.60
p90 = num * 0.90
print(f"30%: {p30}\n60%: {p60}\n90%: {p90}")


#7. Problema

lado = float(input("longitud del lado del cuadradito :) : "))
area = lado ** 2
print(f"El área: {area}")


#8. Problema
nums = []
for i in range(5):
    n = float(input(f"número pa sacar el promedio {i+1}: "))
    nums.append(n)
promedio = sum(nums) / len(nums)
print(f"El promedio de tus numeros pendejos es: {promedio}")


#9. Problema

uni = float(input("valor unitario del coso: "))
cantidad = int(input("cantidad que se compro: "))
subtotal = uni * cantidad
iva = subtotal * 0.16
total = subtotal + iva
print(f"Subtotal: {subtotal}")
print(f"IVA (16%): {iva}")
print(f"Total a pagar: {total}")


#10. Problema

salario_diario = float(input("salario diario: "))
dias = int(input("días trabajados: "))
bruto = salario_diario * dias
pension = bruto * 0.10
descuento_salud = bruto * 0.15
descuentos = pension + descuento_salud
salario_neto = bruto - descuentos

print(f"Salario a pagar (neto): {salario_neto}")


#11. Problema

actual = int(input("Año actual: "))
nac = int(input("Año de nacimiento: "))
edad = actual - nac
if edad >= 18:
    print(f"Tiene {edad} años. Es mayor de edad. Busca un trabajo.")
else:
    print(f"Tiene {edad} años. No es mayor de edad. Compra BitCoins")
  
    
#12. Problema

n = float(input("número: "))
if n > 0:
    print("positivo.")
elif n == 0:
    print("es cero.")
else:
    print("negativo.")
  
    
#13. Problema

a = float(input("primer número: "))
b = float(input("segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{b} es mayor que {a}")
else:
    print("son iguales.")


#14. Problema

grado = int(input("grado del estudiante (en número pendejo): "))
if grado <= 6 and grado >= 1:
    print("El estudiante requiere refrigerio.")
elif grado > 6:
    print("El estudiante NO requiere refrigerio. Comprate una empanada.")
else:
    print("Grado inválido wtf.")


#15. Problema

n = float(input("número: "))
mitad = n / 2
if mitad > 100:
    print(f"La mitad ({mitad}) es mayor que 100.")
elif mitad < 100:
    print(f"La mitad ({mitad}) es menor que 100.")
else:
    print(f"La mitad ({mitad}) es exactamente 100.")
    



