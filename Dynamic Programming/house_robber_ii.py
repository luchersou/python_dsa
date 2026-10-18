# ---------------------------------------------------------------------------
# 213. House Robber II
# As casas estão em círculo: a primeira e a última são vizinhas, então
# nunca podemos roubar as duas. Resolvemos o House Robber normal duas
# vezes (sem a última casa e sem a primeira) e pegamos o maior.
# Tempo: O(n)
# Espaço: O(n) por causa das fatias; O(1) se percorrer por índices
# ---------------------------------------------------------------------------
class Solucao:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sem_a_ultima = self._roubar_em_linha(nums[:-1])
        sem_a_primeira = self._roubar_em_linha(nums[1:])

        return max(sem_a_ultima, sem_a_primeira)

    def _roubar_em_linha(self, casas: list[int]) -> int:
        melhor_dois_atras = 0
        melhor_um_atras = 0

        for dinheiro_da_casa in casas:
            melhor_atual = max(dinheiro_da_casa + melhor_dois_atras, melhor_um_atras)
            melhor_dois_atras = melhor_um_atras
            melhor_um_atras = melhor_atual

        return melhor_um_atras
