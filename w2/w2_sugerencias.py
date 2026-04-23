def repeated_chars(str1: str, str2: str, str3: str) -> list:
    """funcion que va a contar la cantidad de caracteres repetidos en las cadenas recibidas por parametro y devolver una lista con los caracteres repetidos"""
    # Convertir ambas cadenas a conjuntos para obtener los caracteres únicos
    set1 = set(str1)
    set2 = set(str2)
    
    
    # Encontrar la intersección de ambos conjuntos para obtener los caracteres repetidos
    repeated = set1.intersection(set2)
    
    # Convertir el conjunto de caracteres repetidos a una lista y devolverla
    return list(repeated)

if __name__ == "__main__":
    str1 = input("Ingrese la primera cadena: ")
    str2 = input("Ingrese la segunda cadena: ")
    
    result = repeated_chars(str1, str2)
    print("Caracteres repetidos:", result)