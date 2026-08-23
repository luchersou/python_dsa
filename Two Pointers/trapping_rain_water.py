def trap(altura: list[int]) -> int:
    if not altura:
        return 0
    
    esquerda, direita = 0, len(altura) - 1
    max_esquerda, max_direita = altura[esquerda], altura[direita]
    agua_total = 0
    
    while esquerda < direita:
        if max_esquerda < max_direita:
            esquerda += 1
            max_esquerda = max(max_esquerda, altura[esquerda])
            agua_total += max_esquerda - altura[esquerda]
        else:
            direita -= 1
            max_direita = max(max_direita, altura[direita])
            agua_total += max_direita - altura[direita]
    
    return agua_total