def leap_year():
    year=int(input("Ingrese un año aqui:"))
    if(year %4 == 0 and year %100 != 0) or (year %400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
