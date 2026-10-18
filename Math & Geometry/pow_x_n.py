# ---------------------------------------------------------------------------
# 50. Pow(x, n)
# Exponenciação rápida: x^n = (x²)^(n/2). A cada passo o expoente cai
# pela metade; quando ele é ímpar, multiplicamos um x a mais no resultado.
# Expoente negativo: x^(-n) = (1/x)^n.
# Tempo: O(log n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        resultado = 1.0
        base = x
        expoente = n

        while expoente > 0:
            if expoente % 2 == 1:
                resultado *= base
            base *= base
            expoente //= 2

        return resultado
