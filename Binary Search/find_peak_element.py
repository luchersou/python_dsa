def find_peak_element(nums: list[int]) -> int:
    esquerda, direita = 0, len(nums) - 1

    while esquerda < direita:
        meio = (esquerda + direita) // 2

        if nums[meio] > nums[meio + 1]:
            # A descida está à direita do meio, então existe
            # um pico em meio ou à esquerda dele
            direita = meio
        else:
            # nums[meio] < nums[meio + 1]: está subindo,
            # então o pico está à direita
            esquerda = meio + 1

    return esquerda