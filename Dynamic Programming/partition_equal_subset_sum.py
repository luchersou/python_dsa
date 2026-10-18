# ---------------------------------------------------------------------------
# 416. Partition Equal Subset Sum
# Se a soma total for ímpar, é impossível. Senão, a pergunta vira:
# "existe um subconjunto com soma igual à metade?" (mochila 0/1).
# Guardamos o conjunto de todas as somas alcançáveis até agora.
# Tempo: O(n * alvo)   (alvo = soma total / 2)
# Espaço: O(alvo)
# ---------------------------------------------------------------------------
class Solucao:
    def canPartition(self, nums: list[int]) -> bool:
        soma_total = sum(nums)
        if soma_total % 2 == 1:
            return False

        alvo = soma_total // 2
        somas_alcancaveis = {0}

        for numero in nums:
            novas_somas = set()
            for soma in somas_alcancaveis:
                nova_soma = soma + numero
                if nova_soma == alvo:
                    return True
                if nova_soma < alvo:
                    novas_somas.add(nova_soma)

            somas_alcancaveis |= novas_somas

        return alvo in somas_alcancaveis
