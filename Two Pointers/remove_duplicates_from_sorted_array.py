def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    
    # Ponteiro que marca a posição do último elemento único
    posicao_unica = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[posicao_unica]:
            posicao_unica += 1
            nums[posicao_unica] = nums[i]
    
    return posicao_unica + 1