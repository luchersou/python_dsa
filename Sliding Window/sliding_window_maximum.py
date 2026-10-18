from collections import deque

def max_sliding_window(nums, k):
    resultado = []
    indices_candidatos = deque()  # índices em ordem decrescente de valor

    for direita in range(len(nums)):
        esquerda = direita - k + 1  # primeiro índice que ainda pertence à janela

        # Remove do início o índice que já saiu da janela
        if indices_candidatos and indices_candidatos[0] < esquerda:
            indices_candidatos.popleft()

        # Remove do fim os candidatos menores ou iguais ao número novo
        while indices_candidatos and nums[indices_candidatos[-1]] <= nums[direita]:
            indices_candidatos.pop()

        indices_candidatos.append(direita)

        # A janela só está completa a partir do índice k - 1
        if direita >= k - 1:
            resultado.append(nums[indices_candidatos[0]])

    return resultado