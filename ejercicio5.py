# realice un programa q dada una cantidad de bs de su equivalente en dolares y en euros
# $ = 36.5 y euro = 38.7

bolivares = float(input("ingrese la cantidad en bolivares: "))

dolar = bolivares/ 36.5
euro = bolivares/38.7

print(f' su equivalente en dolares es {dolar:.2f}')
print(f' su equivalente en euros es {euro:.2f}')
