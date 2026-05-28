def encontrar_comunes(lista1, lista2):
    # Uso de bucles anidados: Ineficiente en tiempo
    comunes = []
    for item1 in lista1:
        for item2 in lista2:
            if item1 == item2:
                if item1 not in comunes:
                    comunes.append(item1)
    return comunes

nombres_proyectos = ["Alpha", "Beta", "Gamma", "Delta"]
nombres_finalizados = ["Gamma", "Epsilon", "Alpha", "Zeta"]
print(encontrar_comunes(nombres_proyectos, nombres_finalizados))
