def encontrar_comunes(lista1, lista2):
    """
    Encuentra elementos comunes entre dos listas.
    Complejidad: O(n + m) con sets en lugar de O(n*m*k) con bucles anidados.
    """
    return list(set(lista1) & set(lista2))


nombres_proyectos = ["Alpha", "Beta", "Gamma", "Delta"]
nombres_finalizados = ["Gamma", "Epsilon", "Alpha", "Zeta"]
print(encontrar_comunes(nombres_proyectos, nombres_finalizados))
