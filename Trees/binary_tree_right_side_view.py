from collections import deque
 
 
class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
 
 
# ---------------------------------------------------------------------------
# Binary Tree Right Side View
# Imagine olhar a árvore pelo lado direito: em cada nível, só enxergamos o
# nó mais à direita (os outros ficam escondidos atrás dele).
#
# Ideia: é o mesmo percurso por níveis (BFS) do exercício 69. Em cada
# nível, o último nó que sai da fila é o mais à direita, e é ele que
# entra no resultado.
#
# Exemplo:      1            visão pela direita: [1, 3, 4]
#              / \
#             2   3
#              \   \
#               5   4
#
# Tempo: O(n) — visita cada nó uma vez.
# Espaço: O(n) — no pior caso, a fila guarda um nível inteiro.
# ---------------------------------------------------------------------------
def visao_lado_direito(raiz):
    if raiz is None:
        return []
 
    visao = []
    fila = deque([raiz])
 
    while fila:
        tamanho_do_nivel = len(fila)
 
        for posicao in range(tamanho_do_nivel):
            no_atual = fila.popleft()
 
            e_ultimo_do_nivel = posicao == tamanho_do_nivel - 1
            if e_ultimo_do_nivel:
                visao.append(no_atual.valor)
 
            if no_atual.esquerda is not None:
                fila.append(no_atual.esquerda)
            if no_atual.direita is not None:
                fila.append(no_atual.direita)
 
    return visao