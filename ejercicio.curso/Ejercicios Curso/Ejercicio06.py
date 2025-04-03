# pide al usuario un año , determina si es bisiesto si es divisible por 4, excepto si
# es divisible por 100 pero no por 400

año = int(input("Ingrse un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"el año {año} es bisiesto")
else:
    print(f"el año {año} no es bisiesto")
