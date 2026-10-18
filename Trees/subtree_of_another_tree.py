class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


# ---------------------------------------------------------------------------
# 67. Subtree of Another Tree
# sub_raiz é subárvore de raiz se existir algum nó em raiz a partir do qual
# a árvore é exatamente igual (usa sao_iguais) a sub_raiz.
# Tempo: O(n * m) — no pior caso, para cada um dos n nós de raiz,
#        comparamos com os m nós de sub_raiz.
# Espaço: O(h)
# ---------------------------------------------------------------------------
def e_subarvore(raiz, sub_raiz):
    if sub_raiz is None:
        return True
 
    if raiz is None:
        return False
 
    if sao_iguais(raiz, sub_raiz):
        return True
 
    return e_subarvore(raiz.esquerda, sub_raiz) or e_subarvore(raiz.direita, sub_raiz)