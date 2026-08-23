def search_insert(nums: list[int], target: int) -> int:
    esquerda, direita = 0, len(nums) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if nums[meio] == target:
            return meio
        elif nums[meio] < target:
            esquerda = meio + 1
        else:
            direita = meio - 1

    # Se não achou, 'esquerda' parou exatamente na posição
    # onde o elemento deveria ser inserido
    return esquerda