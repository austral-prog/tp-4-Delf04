def leap_year():

    año_bisiesto = int(input("Ingrese un año: "))

    if año_bisiesto % 4 == 0 and año_bisiesto % 100 != 0 or año_bisiesto % 400 == 0:
       print(f"El año {año_bisiesto} es bisiesto")
    else:
       print(f"El año {año_bisiesto} no es bisiesto")
