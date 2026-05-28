class CardValidator:
    """Valida números de tarjeta usando el algoritmo de Luhn.

    Instanciar con la cadena que contiene el número de tarjeta (puede incluir
    espacios u otros caracteres). Usar `validate()` para comprobar si el
    número es probablemente válido según Luhn.
    """

    def __init__(self, c_num: str):
        # `raw` guarda el valor original tal como fue recibido
        self.raw = c_num

    def clear(self) -> str:
        """Devuelve sólo los dígitos del valor original.

        Recorre la cadena original y concatena únicamente los caracteres
        que son dígitos, ignorando espacios, guiones u otros símbolos.
        """
        res = ""
        for c in self.raw:
            if c.isdigit():
                res += c
        return res

    def validate(self) -> bool:
        """Valida el número de tarjeta usando el algoritmo de Luhn.

        Pasos principales:
        - Limpiar la entrada dejando sólo dígitos.
        - Comprobar longitud mínima/máxima razonable (13-19 dígitos).
        - Aplicar Luhn: invertir los dígitos, duplicar cada segundo dígito
          (desde la derecha), restar 9 si el resultado es mayor que 9,
          sumar todos los dígitos y verificar que la suma sea múltiplo de 10.

        Devuelve True si pasa la comprobación de Luhn, False en caso
        contrario (o si la entrada no tiene una longitud válida).
        """
        d = self.clear()

        # Un número de tarjeta típicamente tiene entre 13 y 19 dígitos.
        if not d or len(d) < 13 or len(d) > 19:
            return False

        s = 0
        # Trabajamos desde la derecha hacia la izquierda; invertir facilita
        # aplicar la regla de duplicar cada segundo dígito.
        r = d[::-1]

        for i in range(len(r)):
            # n es el dígito actual (como entero)
            n = int(r[i])

            # En posiciones impares (segunda, cuarta, ...) desde la derecha
            # duplicamos el dígito según la regla de Luhn.
            if i % 2 == 1:
                n *= 2
                # Si al duplicar obtenemos >= 10, sumamos los dígitos del
                # resultado; restar 9 es equivalente a hacerlo (por ejemplo,
                # 12 -> 1 + 2 = 3 ; 12 - 9 = 3).
                if n > 9:
                    n -= 9

            s += n

        # Si la suma total es múltiplo de 10, el número pasa la comprobación.
        return s % 10 == 0