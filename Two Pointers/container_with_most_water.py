def max_area(altura: list[int]) -> int:
    esquerda, direita = 0, len(altura) - 1
    maior_area = 0
    
    while esquerda < direita:
        largura = direita - esquerda
        altura_limite = min(altura[esquerda], altura[direita])
        area_atual = largura * altura_limite
        
        maior_area = max(maior_area, area_atual)
        
        # Move o ponteiro da menor altura — é o único que pode melhorar
        if altura[esquerda] < altura[direita]:
            esquerda += 1
        else:
            direita -= 1
    
    return maior_area