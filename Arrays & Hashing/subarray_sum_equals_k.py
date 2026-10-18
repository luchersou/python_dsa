from collections import defaultdict


# ---------------------------------------------------------------------------
# 560. Subarray Sum Equals K
# Soma de prefixos: a soma do subarray (i, j] é prefixo[j] - prefixo[i].
# Queremos prefixo[j] - prefixo[i] == k, ou seja, prefixo[i] == prefixo[j] - k.
# Contamos quantas vezes cada soma de prefixo já apareceu.
# (Janela deslizante não funciona aqui porque pode haver números negativos.)
# Tempo: O(n)
# Espaço: O(n)
# ---------------------------------------------------------------------------
def subarray_sum(nums: list[int], k: int) -> int:
    vezes_que_apareceu = defaultdict(int)
    vezes_que_apareceu[0] = 1  # prefixo vazio, para subarrays que começam no índice 0

    soma_atual = 0
    total_subarrays = 0

    for numero in nums:
        soma_atual += numero
        total_subarrays += vezes_que_apareceu[soma_atual - k]
        vezes_que_apareceu[soma_atual] += 1

    return total_subarrays
