# Crea un programa que pida el ususriodos numeros y un operador , realiza la operacion 
# correspondiente e imprime el resultado 
 
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
operador = input("Ingresa un operador (+, -, /, *): ") 

if operador == '+':
    print(num1 + num2)
elif operador == '-': 
    print(num1 - num2)
elif operador == '/': 
    print(num1 / num2)
elif operador == '*': 
    print(num1 * num2)
else:
    print("El operador no es valido")
 
