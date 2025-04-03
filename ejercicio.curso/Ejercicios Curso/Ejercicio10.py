# pide al usuario una duracion en horas , minutos y segundos , calcula la duracion total
#en segundo e imprime el resultado

hora = int(input("Ingrese una cantidad de horas: "))
min = int(input("Ingrese una cantidad de minutos: "))
segundos = int(input("ingrese una cantidad de segundos: "))

hora_seg = hora * 3600 
min_seg = min * 60 

duracion_total = hora_seg + min_seg + segundos
print("La duracion total en segundos es: ", duracion_total)