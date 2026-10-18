class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
        

# ---------------------------------------------------------------------------
# 66. Same Tree
# Duas árvores são iguais se tiverem a mesma estrutura e os mesmos valores
# em cada posição.
# Tempo: O(n)
# Espaço: O(h)
# ---------------------------------------------------------------------------
def sao_iguais(raiz1, raiz2):
    if raiz1 is None and raiz2 is None:
        return True
 
    if raiz1 is None or raiz2 is None:
        return False
 
    if raiz1.valor != raiz2.valor:
        return False
 
    return (
        sao_iguais(raiz1.esquerda, raiz2.esquerda)
        and sao_iguais(raiz1.direita, raiz2.direita)
    )