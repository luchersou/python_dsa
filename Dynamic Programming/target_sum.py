# ---------------------------------------------------------------------------
# 494. Target Sum
# Dividimos os números em positivos (P) e negativos (N):
#   P - N = alvo  e  P + N = soma_total  =>  P = (alvo + soma_total) / 2
# O problema vira: quantos subconjuntos somam P? (mochila 0/1 de contagem)
# Percorremos os valores de trás para frente para não reutilizar o mesmo
# número duas vezes.
# Tempo: O(n * P)
# Espaço: O(P)
# ---------------------------------------------------------------------------
class Solucao:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        soma_total = sum(nums)

        if abs(target) > soma_total or (target + soma_total) % 2 == 1:
            return 0

        soma_positivos = (target + soma_total) // 2
        formas = [1] + [0] * soma_positivos

        for numero in nums:
            for valor in range(soma_positivos, numero - 1, -1):
                formas[valor] += formas[valor - numero]

        return formas[soma_positivos]
