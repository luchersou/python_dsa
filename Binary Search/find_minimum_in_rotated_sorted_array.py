def find_min(nums: list[int]) -> int:
    esquerda, direita = 0, len(nums) - 1

    while esquerda < direita:
        meio = (esquerda + direita) // 2

        if nums[meio] > nums[direita]:
            # o mínimo está na metade direita
            esquerda = meio + 1
        else:
            # o mínimo está na metade esquerda (ou é o próprio meio)
            direita = meio

    return nums[esquerda]