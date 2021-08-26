"""
#Automatico del 1 al 10
c = 0
while c < 10:
    c +=1
    print("Valor de c", c)
"""

n = int(input("Ingrese un número: "))

suma = 0
menores = 0

while menores < n:
    suma += menores
    menores +=1

print("La suma es: ", suma)