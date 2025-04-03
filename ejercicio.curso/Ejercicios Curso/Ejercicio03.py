# Pide al usuario una temperatura en grados Celsius, Comvierte la temperatura
#a grados Fahrenheit (Fahrenheit = (Celsius* 9/5)+32) e imprime el resultado

temperatura = int(input("Ingrese la tempratura en Celsius: "))

F = (temperatura * 1.8) + 32 
print("La temperatura en fahrenheit es: ", F)
