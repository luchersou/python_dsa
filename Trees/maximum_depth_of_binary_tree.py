class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


# ---------------------------------------------------------------------------
# 63. Maximum Depth of Binary Tree
# Profundidade máxima = 1 + a maior profundidade entre as duas subárvores.
# Tempo: O(n)
# Espaço: O(h)
# ---------------------------------------------------------------------------
def profundidade_maxima(raiz):
    if raiz is None:
        return 0
 
    profundidade_esquerda = profundidade_maxima(raiz.esquerda)
    profundidade_direita = profundidade_maxima(raiz.direita)
 
    return 1 + max(profundidade_esquerda, profundidade_direita)
 