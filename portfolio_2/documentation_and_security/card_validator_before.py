class CardValidator:
    def __init__(self, c_num: str):
        self.raw = c_num

    def clear(self) -> str:
        res = ""
        for c in self.raw:
            if c.isdigit():
                res += c
        return res

    def validate(self) -> bool:
        d = self.clear()
        
        if not d or len(d) < 13 or len(d) > 19:
            return False

        s = 0
        r = d[::-1]

        for i in range(len(r)):
            n = int(r[i])

            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            
            s += n

        return s % 10 == 0