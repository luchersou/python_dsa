# ---------------------------------------------------------------------------
# 136. Single Number
# XOR tem duas propriedades úteis: a ^ a = 0 e a ^ 0 = a. Fazendo XOR de
# todos os números, os pares se anulam e sobra só o que aparece uma vez.
# Tempo: O(n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def singleNumber(self, nums: list[int]) -> int:
        resultado = 0

        for numero in nums:
            resultado ^= numero

        return resultado
