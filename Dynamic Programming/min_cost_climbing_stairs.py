# ---------------------------------------------------------------------------
# 746. Min Cost Climbing Stairs
# custo_minimo(i) = custo[i] + min(custo_minimo(i-1), custo_minimo(i-2)).
# O topo fica depois do último degrau, então a resposta é o menor entre
# os dois últimos degraus.
# Tempo: O(n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        custo_dois_atras = 0
        custo_um_atras = 0

        for custo_degrau in cost:
            custo_atual = custo_degrau + min(custo_um_atras, custo_dois_atras)
            custo_dois_atras = custo_um_atras
            custo_um_atras = custo_atual

        # Podemos pular para o topo a partir de qualquer um dos dois últimos degraus
        return min(custo_um_atras, custo_dois_atras)
