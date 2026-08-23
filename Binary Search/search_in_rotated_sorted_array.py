def search(nums: list[int], target: int) -> int:
    esquerda, direita = 0, len(nums) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if nums[meio] == target:
            return meio

        # Descobre qual metade está ordenada
        if nums[esquerda] <= nums[meio]:
            # metade esquerda está ordenada
            if nums[esquerda] <= target < nums[meio]:
                direita = meio - 1
            else:
                esquerda = meio + 1
        else:
            # metade direita está ordenada
            if nums[meio] < target <= nums[direita]:
                esquerda = meio + 1
            else:
                direita = meio - 1

    return -1