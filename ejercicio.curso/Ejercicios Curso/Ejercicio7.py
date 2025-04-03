# pide al usuario el precio de un producto y el porcentaje de descuento , 
# calcula el precio final despues del descuento e imprime el resulto

precio_inicial = float(input("escribe el precio del prducto: "))
porcetaje_des = int(input("ingrese el porcentaje de descuesto: "))

precio_final = precio_inicial - ((porcetaje_des / 100) * precio_inicial) 
print(f"el precio final a pagar es: {precio_final} ")

