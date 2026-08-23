# ---------------------------------------------------------------------------
# 74. Construct Binary Tree from Preorder and Inorder Traversal
# Ideia central:
# - O primeiro valor da pré-ordem é sempre a raiz da (sub)árvore atual.
# - Achando esse valor na in-ordem, tudo que está à esquerda dele na
#   in-ordem pertence à subárvore esquerda, e tudo à direita pertence à
#   subárvore direita.
# - Repetimos isso recursivamente, "fatiando" as duas listas.
#
# Pré-processamos um dicionário (valor -> índice na in-ordem) para não
# precisar procurar o índice com uma busca linear a cada chamada.
# Tempo: O(n)
# Espaço: O(n)
# ---------------------------------------------------------------------------
def construir_arvore(preordem, inordem):
    indice_na_inordem = {valor: indice for indice, valor in enumerate(inordem)}
    ponteiro_preordem = 0
 
    def construir(inicio_inordem, fim_inordem):
        nonlocal ponteiro_preordem
 
        if inicio_inordem > fim_inordem:
            return None
 
        valor_raiz = preordem[ponteiro_preordem]
        ponteiro_preordem += 1
 
        raiz = No(valor_raiz)
 
        indice_raiz = indice_na_inordem[valor_raiz]
 
        raiz.esquerda = construir(inicio_inordem, indice_raiz - 1)
        raiz.direita = construir(indice_raiz + 1, fim_inordem)
 
        return raiz
 
    return construir(0, len(inordem) - 1)