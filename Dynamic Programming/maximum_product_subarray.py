# ---------------------------------------------------------------------------
# 152. Maximum Product Subarray
# Um número negativo transforma o menor produto no maior. Por isso
# guardamos tanto o maior quanto o menor produto terminando na posição
# atual.
# Tempo: O(n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def maxProduct(self, nums: list[int]) -> int:
        maior_produto_geral = nums[0]
        maior_ate_aqui = nums[0]
        menor_ate_aqui = nums[0]

        for numero in nums[1:]:
            candidatos = (numero, numero * maior_ate_aqui, numero * menor_ate_aqui)
            maior_ate_aqui = max(candidatos)
            menor_ate_aqui = min(candidatos)

            maior_produto_geral = max(maior_produto_geral, maior_ate_aqui)

        return maior_produto_geral
