class CardValidator:
    """Valida números de tarjeta usando el algoritmo de Luhn.

    Atributos:
        raw (str): La entrada original (puede contener espacios o guiones).

    Métodos:
        clear(): Devuelve sólo los dígitos extraídos de `raw`.
        validate(): Comprueba si el número de tarjeta es válido según Luhn.
    """

    def __init__(self, c_num: str):
        # Guardamos la cadena original tal cual fue recibida
        self.raw = c_num

    def clear(self) -> str:
        """Extrae y devuelve sólo los caracteres numéricos de la entrada.

        Esto permite aceptar entradas con espacios o guiones, por ejemplo
        "4242 4242 4242 4242" o "4242-4242-4242-4242".
        """
        res = ""
        for c in self.raw:
            if c.isdigit():
                res += c
        return res

    def validate(self) -> bool:
        """Valida el número de tarjeta aplicando el algoritmo de Luhn.

        Pasos:
        1. Limpiar la entrada dejando sólo dígitos.
        2. Rechazar si la longitud está fuera del rango razonable (13-19).
        3. Recorrer los dígitos de derecha a izquierda, doblando cada segundo
           dígito; si el resultado de doblar es mayor que 9, restar 9
           (equivalente a sumar sus dígitos). Sumar todos los valores.
        4. Si la suma total es divisible por 10, el número pasa la comprobación.

        Retorna:
            bool: True si el número es válido según Luhn, False en caso contrario.
        """
        d = self.clear()

        # Rechazamos entradas vacías o con longitud improbable para tarjetas
        if not d or len(d) < 13 or len(d) > 19:
            return False

        s = 0
        # Invertimos la cadena para procesar desde el dígito menos significativo
        r = d[::-1]

        for i in range(len(r)):
            n = int(r[i])

            # Para cada segundo dígito (posición impar en la cadena invertida)
            # se dobla su valor.
            if i % 2 == 1:
                n *= 2
                # Si doblar produce un número de dos dígitos, restamos 9
                # (por ejemplo 12 -> 1 + 2 = 3; 12 - 9 = 3)
                if n > 9:
                    n -= 9

            s += n

        # Si la suma total es divisible por 10, el número es válido
        return s % 10 == 0