def move_zeroes(nums: list[int]) -> None:
    # Ponteiro que marca onde o próximo número não-zero deve ir
    posicao_livre = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[posicao_livre], nums[i] = nums[i], nums[posicao_livre]
            posicao_livre += 1