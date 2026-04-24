def calcular_area_cuadrado(lado):
    if lado <= 0:
        print("Error: El valor debe ser positivo")
        return
    area = lado * lado
    print(f"El resultado del cálculo es: {area}")
    return area

def calcular_area_rectangulo(base, altura):
    if base <= 0 or altura <= 0:
        print("Error: El valor debe ser positivo")
        return
    area = base * altura
    print(f"El resultado del cálculo es: {area}")
    return area

def calcular_area_circulo(radio):
    if radio <= 0:
        print("Error: El valor debe ser positivo")
        return
    import math
    area = math.pi * (radio ** 2)
    print(f"El resultado del cálculo es: {area}")
    return area