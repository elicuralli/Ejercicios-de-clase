#Realiza un programa que muestre el precio del IVA de un producto con un valor de 100 y
#su precio final.

producto = float(input("ingrese precio de producto: "))

precioT = producto + (producto*0.16)

#print("su precio total es: ", str(precioT))
print(f'Precio del producto: {precioT:.2f}')