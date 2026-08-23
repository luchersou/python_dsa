# ---------------------------------------------------------------------------
# 69. Binary Tree Level Order Traversal
# Percorre a árvore nível por nível (BFS), usando uma fila.
# Em cada volta do laço externo, processamos exatamente os nós do nível
# atual (guardando quantos são antes de começar a esvaziar a fila).
# Tempo: O(n)
# Espaço: O(n) — no pior caso, o último nível pode ter até metade dos nós.
# ---------------------------------------------------------------------------
def travessia_em_nivel(raiz):
    if raiz is None:
        return []
 
    resultado = []
    fila = deque([raiz])
 
    while fila:
        tamanho_do_nivel = len(fila)
        valores_do_nivel = []
 
        for _ in range(tamanho_do_nivel):
            no_atual = fila.popleft()
            valores_do_nivel.append(no_atual.valor)
 
            if no_atual.esquerda is not None:
                fila.append(no_atual.esquerda)
            if no_atual.direita is not None:
                fila.append(no_atual.direita)
 
        resultado.append(valores_do_nivel)
 
    return resultado