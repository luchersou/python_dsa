# ---------------------------------------------------------------------------
# 268. Missing Number
# Fazemos XOR de todos os índices 0..n com todos os valores do array.
# Cada número presente aparece duas vezes (como índice e como valor) e
# se anula; sobra só o que está faltando.
# Tempo: O(n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def missingNumber(self, nums: list[int]) -> int:
        resultado = len(nums)  # o índice n não aparece no enumerate

        for indice, numero in enumerate(nums):
            resultado ^= indice ^ numero

        return resultado
