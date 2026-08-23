def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    resultado = []
    n = len(nums)
    
    for i in range(n):
        # Evita repetir a primeira âncora
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n):
            # Evita repetir a segunda âncora
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            esquerda, direita = j + 1, n - 1
            
            while esquerda < direita:
                soma = nums[i] + nums[j] + nums[esquerda] + nums[direita]
                
                if soma < target:
                    esquerda += 1
                elif soma > target:
                    direita -= 1
                else:
                    resultado.append([nums[i], nums[j], nums[esquerda], nums[direita]])
                    esquerda += 1
                    direita -= 1
                    while esquerda < direita and nums[esquerda] == nums[esquerda - 1]:
                        esquerda += 1
                    while esquerda < direita and nums[direita] == nums[direita + 1]:
                        direita -= 1
    
    return resultado