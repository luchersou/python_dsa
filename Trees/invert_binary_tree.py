class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


# ---------------------------------------------------------------------------
# 62. Invert Binary Tree
# Espelha a árvore: troca a subárvore esquerda com a direita, em cada nó.
# Tempo: O(n) — visita cada nó uma vez.
# Espaço: O(h) — altura da árvore, por causa da pilha de recursão.
# ---------------------------------------------------------------------------
def inverter_arvore(raiz):
    if raiz is None:
        return None
 
    raiz.esquerda, raiz.direita = raiz.direita, raiz.esquerda
 
    inverter_arvore(raiz.esquerda)
    inverter_arvore(raiz.direita)
 
    return raiz