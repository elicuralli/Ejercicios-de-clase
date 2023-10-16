#Realiza un programa que, dado como datos el radio y la altura de un cilindro, calcule e
#imprima el área y su volumen.

pi = 3.1416
cilindro_radio = float(input("ingrese el radio del cilindro: "))
cilindro_altura = float(input("ingrese la altura del cilindro: "))

area = 2*pi*cilindro_radio*cilindro_altura+ 2*pi*cilindro_radio**2
volumen = pi*cilindro_radio**2*cilindro_altura

print(f'el area del cilindro es {area:.2f}')
print(f'el volumen del cilindro es {volumen:.2f}')
