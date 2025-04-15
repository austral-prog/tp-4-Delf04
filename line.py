def line():
    import math 
    
    coe_a = float(input("Ingrese el coeficiente A: "))
    coe_b = float(input("Ingrese el coeficiente B: "))
    coe_x1 = float(input("Ingrese el coeficiente X1: "))
    coe_x2 = float(input("Ingrese el coeficiente X2: "))

    print(f"El coeficiente A de su ecuación de la recta es: {coe_a}")
    print(f"El coeficiente B de su ecuación de la recta es: {coe_b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coe_x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coe_x2}")

    ecuacion = (f"Y = {coe_a}X + {coe_b}")

    print("\nPara la siguiente ecuación:")
    print(f"\t{ecuacion}\n")

    y1 = (coe_a*coe_x1 + coe_b)
    y2 = (coe_a*coe_x2 + coe_b)

    print("Dados los siguientes puntos:")
    print(f"\tP1 ({coe_x1}, {y1})")
    print(f"\tP2 ({coe_x2}, {y2})")

    distancia = math.sqrt((coe_x2 - coe_x1)**2 + (y2 - y1)**2)
    print(f"\nLa distancia entre ellos es: {distancia}")
