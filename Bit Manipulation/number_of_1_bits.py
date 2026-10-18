# ---------------------------------------------------------------------------
# 191. Number of 1 Bits
# n & (n - 1) apaga o bit 1 mais à direita de n. Contamos quantas vezes
# conseguimos fazer isso até n virar zero.
# Tempo: O(k)   (k = quantidade de bits 1, no máximo 32)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def hammingWeight(self, n: int) -> int:
        quantidade_de_uns = 0

        while n:
            n &= n - 1
            quantidade_de_uns += 1

        return quantidade_de_uns
