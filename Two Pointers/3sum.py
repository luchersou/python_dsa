def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    resultado = []
    
    for i in range(len(nums)):
        # Evita repetir o mesmo número como "âncora"
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        esquerda, direita = i + 1, len(nums) - 1
        
        while esquerda < direita:
            soma = nums[i] + nums[esquerda] + nums[direita]
            
            if soma < 0:
                esquerda += 1
            elif soma > 0:
                direita -= 1
            else:
                resultado.append([nums[i], nums[esquerda], nums[direita]])
                esquerda += 1
                direita -= 1
                # Pula duplicatas depois de achar um trio válido
                while esquerda < direita and nums[esquerda] == nums[esquerda - 1]:
                    esquerda += 1
                while esquerda < direita and nums[direita] == nums[direita + 1]:
                    direita -= 1
    
    return resultado