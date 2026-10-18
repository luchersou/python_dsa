# ---------------------------------------------------------------------------
# 198. House Robber
# Em cada casa decidimos: roubar (valor da casa + melhor até duas casas
# atrás) ou pular (melhor até a casa anterior).
# Tempo: O(n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def rob(self, nums: list[int]) -> int:
        melhor_dois_atras = 0
        melhor_um_atras = 0

        for dinheiro_da_casa in nums:
            melhor_atual = max(dinheiro_da_casa + melhor_dois_atras, melhor_um_atras)
            melhor_dois_atras = melhor_um_atras
            melhor_um_atras = melhor_atual

        return melhor_um_atras
