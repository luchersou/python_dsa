def sort_colors(nums: list[int]) -> None:
    # Três ponteiros: baixo (zeros), meio (percorre), alto (dois)
    baixo, meio, alto = 0, 0, len(nums) - 1
    
    while meio <= alto:
        if nums[meio] == 0:
            nums[baixo], nums[meio] = nums[meio], nums[baixo]
            baixo += 1
            meio += 1
        elif nums[meio] == 1:
            meio += 1
        else:  # nums[meio] == 2
            nums[meio], nums[alto] = nums[alto], nums[meio]
            alto -= 1
            # Não avança 'meio' aqui — o valor trocado pra cá ainda não foi checado
    
    return None