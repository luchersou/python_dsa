from bisect import bisect_left


# ---------------------------------------------------------------------------
# 300. Longest Increasing Subsequence
# menores_finais[k] guarda o menor valor possível que termina uma
# subsequência crescente de tamanho k+1. Para cada número, achamos via
# busca binária onde ele entra: ou estende a maior subsequência, ou
# substitui um final por um valor menor (deixando mais espaço para crescer).
# Tempo: O(n log n)
# Espaço: O(n)
# ---------------------------------------------------------------------------
class Solucao:
    def lengthOfLIS(self, nums: list[int]) -> int:
        menores_finais = []

        for numero in nums:
            posicao = bisect_left(menores_finais, numero)

            if posicao == len(menores_finais):
                menores_finais.append(numero)
            else:
                menores_finais[posicao] = numero

        return len(menores_finais)
