# ---------------------------------------------------------------------------
# 70. Climbing Stairs
# Para chegar ao degrau i, ou viemos do degrau i-1 (1 passo) ou do i-2
# (2 passos). Logo, formas(i) = formas(i-1) + formas(i-2), que é Fibonacci.
# Só precisamos guardar os dois últimos valores.
# Tempo: O(n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def climbStairs(self, n: int) -> int:
        formas_dois_atras = 1  # formas de chegar ao degrau 0
        formas_um_atras = 1    # formas de chegar ao degrau 1

        for _ in range(2, n + 1):
            formas_atual = formas_um_atras + formas_dois_atras
            formas_dois_atras = formas_um_atras
            formas_um_atras = formas_atual

        return formas_um_atras
