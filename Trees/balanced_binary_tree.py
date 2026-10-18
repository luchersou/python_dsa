class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


# ---------------------------------------------------------------------------
# 65. Balanced Binary Tree
# Uma árvore é balanceada se, para todo nó, a diferença de altura entre as
# subárvores esquerda e direita for no máximo 1.
# Usamos -1 como um "sinal de desequilíbrio encontrado" para poder parar
# de recalcular alturas assim que descobrimos que não está balanceada.
# Tempo: O(n)
# Espaço: O(h)
# ---------------------------------------------------------------------------
def e_balanceada(raiz):
    def altura(no):
        if no is None:
            return 0
 
        altura_esquerda = altura(no.esquerda)
        if altura_esquerda == -1:
            return -1
 
        altura_direita = altura(no.direita)
        if altura_direita == -1:
            return -1
 
        if abs(altura_esquerda - altura_direita) > 1:
            return -1
 
        return 1 + max(altura_esquerda, altura_direita)
 
    return altura(raiz) != -1