import re

class PasswordStrengthChecker:
    """
    Clase para evaluar la seguridad de una contraseña basándose en múltiples
    reglas de negocio y retornar un diagnóstico de su fortaleza.
    """
    
    # Lista de contraseñas comunes o prohibidas (Diccionario básico)
    COMMON_PASSWORDS = {
        "123456", "password", "qwerty", "admin123", "contraseña", 
        "123456789", "hola123", "password123", "security"
    }

    def __init__(self, min_length: int = 8):
        if min_length < 4:
            raise ValueError("La longitud mínima no puede ser menor a 4 caracteres.")
        self.min_length = min_length

    def check_strength(self, password: str) -> str:
        """
        Evalúa la contraseña y devuelve un string con la fortaleza:
        'MUY DÉBIL', 'DÉBIL', 'MEDIANA' o 'FUERTE'.
        """
        # 1. Validación de tipo de dato
        if not isinstance(password, str):
            raise TypeError("La contraseña debe ser una cadena de texto (string).")

        # 2. Caso Crítico: Contraseñas vacías o con puros espacios
        if not password.strip():
            return "MUY DÉBIL"

        # 3. Caso Crítico: Contraseñas extremadamente comunes o predecibles
        if password.lower() in self.COMMON_PASSWORDS:
            return "MUY DÉBIL"

        # 4. Caso Crítico: Menor a la longitud mínima configurada
        if len(password) < self.min_length:
            return "DÉBIL"

        # Sistema de puntuación para los criterios cumplidos
        score = 0
        
        # Criterio A: Mezcla de Mayúsculas y Minúsculas
        if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
            score += 1
            
        # Criterio B: Contiene al menos un número
        if re.search(r'[0-9]', password):
            score += 1
            
        # Criterio C: Contiene al menos un carácter especial
        if re.search(r'[^a-zA-Z0-9]', password):
            score += 1
            
        # Criterio D: Longitud extra (Premio a contraseñas largas)
        if len(password) >= self.min_length + 4:
            score += 1

        # 5. Determinación del resultado según el score obtenido
        if score <= 1:
            return "DÉBIL"
        elif score == 2:
            return "MEDIANA"
        else:
            return "FUERTE"