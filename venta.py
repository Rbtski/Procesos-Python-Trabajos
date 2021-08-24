#Mensaje de la Aplicacion
print("Realizando una venta")

#Entrada de datos
vv = float(input("Ingrese Valor de Venta: "))

#Operacion
igv = vv * 0.18
pv = vv + igv

#Salida de datos
print("="*25) #separador
print("Factura de Venta")
print("="*25) #separador
print("Valor venta: ", vv) #
print("IGV: ", igv)
print("Precio de venta: ", pv)
print("="*25) #separador

