# ---------------------------------------------------------------------------
# 338. Counting Bits
# numero >> 1 é o número sem o último bit, e já foi calculado antes.
# Então: bits(numero) = bits(numero >> 1) + (último bit de numero).
# Tempo: O(n)
# Espaço: O(n) para o resultado
# ---------------------------------------------------------------------------
class Solucao:
    def countBits(self, n: int) -> list[int]:
        quantidade_de_uns = [0] * (n + 1)

        for numero in range(1, n + 1):
            quantidade_de_uns[numero] = quantidade_de_uns[numero >> 1] + (numero & 1)

        return quantidade_de_uns
