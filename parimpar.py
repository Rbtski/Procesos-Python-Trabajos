n = int(input("Ingrese Un Numero Entero: "))

#Operaciones
if n!= 0:
    if n > 0: #mayor a 0
       if n % 2 == 0: #True
         print(f"El Numero {n} es Par Positivo")
       else:    
         print(f"El Numero {n} es Impar Positivo")
    else: #si es menor a 0
       if n % 2 == 0: #True
          print(f"El Numero {n} es Par Negativo")
       else:    
          print(f"El Numero {n} es Impar Negativo")
else:
     print(f"El Numero {n} es Neutro")


