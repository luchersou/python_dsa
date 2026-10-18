class No:
    """Nó de uma árvore binária."""

    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


# ---------------------------------------------------------------------------
# 236. Lowest Common Ancestor of a Binary Tree
# Diferente da BST, aqui os valores não dizem para que lado ir, então
# procuramos p e q nos dois lados.
# - Se o nó atual é p ou q, ele mesmo é a resposta para essa subárvore.
# - Se p está de um lado e q do outro, o nó atual é o LCA.
# - Se os dois estão do mesmo lado, repassamos o que aquele lado achou.
# Tempo: O(n)
# Espaço: O(h) da pilha de recursão
# ---------------------------------------------------------------------------
def menor_ancestral_comum(raiz, p, q):
    if raiz is None or raiz is p or raiz is q:
        return raiz

    achado_esquerda = menor_ancestral_comum(raiz.esquerda, p, q)
    achado_direita = menor_ancestral_comum(raiz.direita, p, q)

    if achado_esquerda is not None and achado_direita is not None:
        return raiz

    return achado_esquerda if achado_esquerda is not None else achado_direita
