def two_sum(nums, target):
    # Guarda cada número já visto e seu índice
    vistos = {}  # valor -> índice
    
    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in vistos:
            return [vistos[complemento], i]
        vistos[num] = i
    
    return []  # não encontrou par