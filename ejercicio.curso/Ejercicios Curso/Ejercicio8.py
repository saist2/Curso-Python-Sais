# Pide al usuario su peso en kilogramos y su altura en metros
#calcula si IMC (IMC=peso/(altura**2)) e imprime el resultado }

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso // (altura ** 2) # la segunda barra redondea el resultado 
print(f"Su indice de masa corporal es {imc}")
