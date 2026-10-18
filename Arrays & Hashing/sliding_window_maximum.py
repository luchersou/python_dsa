from collections import deque


# ---------------------------------------------------------------------------
# 239. Sliding Window Maximum
# Mantemos um deque de ÍNDICES cujos valores estão em ordem decrescente.
# - Antes de inserir, removemos do fim quem é menor que o novo valor
#   (esses nunca mais serão o máximo enquanto o novo estiver na janela).
# - Removemos do início o índice que saiu da janela.
# O máximo da janela é sempre o primeiro do deque.
# Tempo: O(n)   (cada índice entra e sai do deque no máximo uma vez)
# Espaço: O(k)
# ---------------------------------------------------------------------------
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    candidatos = deque()
    maximos = []

    for indice, numero in enumerate(nums):
        while candidatos and nums[candidatos[-1]] < numero:
            candidatos.pop()
        candidatos.append(indice)

        # O primeiro candidato ficou para trás da janela
        if candidatos[0] <= indice - k:
            candidatos.popleft()

        # A janela só está completa a partir do índice k - 1
        if indice >= k - 1:
            maximos.append(nums[candidatos[0]])

    return maximos
