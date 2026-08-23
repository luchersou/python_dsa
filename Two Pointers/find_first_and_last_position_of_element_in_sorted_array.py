def search_range(nums: list[int], target: int) -> list[int]:
    primeira = encontrar_borda(nums, target, buscar_primeira=True)
    
    if primeira == -1:
        return [-1, -1]
    
    ultima = encontrar_borda(nums, target, buscar_primeira=False)
    return [primeira, ultima]


def encontrar_borda(nums: list[int], target: int, buscar_primeira: bool) -> int:
    esquerda, direita = 0, len(nums) - 1
    resultado = -1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if nums[meio] < target:
            esquerda = meio + 1
        elif nums[meio] > target:
            direita = meio - 1
        else:
            resultado = meio  # achou o target, mas continua procurando a borda
            if buscar_primeira:
                direita = meio - 1  # tenta achar uma ocorrência mais à esquerda
            else:
                esquerda = meio + 1  # tenta achar uma ocorrência mais à direita
    
    return resultado