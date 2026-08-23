# ---------------------------------------------------------------------------
# 68. Lowest Common Ancestor of a Binary Search Tree
# Como é uma BST (esquerda < nó < direita), não precisamos procurar nos
# dois lados como numa árvore binária qualquer: dá pra usar os valores
# para "descer" na direção certa.
# - Se p e q são menores que o nó atual, o ancestral comum está à esquerda.
# - Se p e q são maiores, está à direita.
# - Caso contrário, os caminhos até p e q se separam aqui: este é o LCA.
# Tempo: O(h) — desce pela altura da árvore.
# Espaço: O(1) — versão iterativa, sem pilha de recursão.
# ---------------------------------------------------------------------------
def menor_ancestral_comum_bst(raiz, p, q):
    no_atual = raiz
 
    while no_atual is not None:
        if p.valor < no_atual.valor and q.valor < no_atual.valor:
            no_atual = no_atual.esquerda
        elif p.valor > no_atual.valor and q.valor > no_atual.valor:
            no_atual = no_atual.direita
        else:
            return no_atual
 
    return None