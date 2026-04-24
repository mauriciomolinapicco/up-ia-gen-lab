import math


def validar_valores_positivos(*valores):
    """Valida que todos los valores sean positivos."""
    for valor in valores:
        if valor <= 0:
            print("Error: El valor debe ser positivo")
            return False
    return True


def imprimir_resultado(area):
    """Imprime el resultado del cálculo de área."""
    print(f"El resultado del cálculo es: {area}")


def calcular_area_cuadrado(lado):
    if not validar_valores_positivos(lado):
        return
    area = lado * lado
    imprimir_resultado(area)
    return area


def calcular_area_rectangulo(base, altura):
    if not validar_valores_positivos(base, altura):
        return
    area = base * altura
    imprimir_resultado(area)
    return area


def calcular_area_circulo(radio):
    if not validar_valores_positivos(radio):
        return
    area = math.pi * (radio ** 2)
    imprimir_resultado(area)
    return area