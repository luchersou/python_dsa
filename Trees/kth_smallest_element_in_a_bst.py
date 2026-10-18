class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
 
 
# ---------------------------------------------------------------------------
# Kth Smallest Element in a BST
# Numa BST, o percurso em ordem (esquerda -> nó -> direita) visita os
# valores em ordem crescente. Então o k-ésimo menor é simplesmente o
# k-ésimo nó visitado nesse percurso.
#
# Fazemos o percurso de forma iterativa, com uma pilha, para poder PARAR
# assim que chegarmos no k-ésimo nó, sem percorrer a árvore inteira.
#
# Passo a passo:
#   1. Desce o máximo possível pela esquerda, empilhando os nós no caminho.
#   2. Desempilha um nó: esse é o próximo menor valor. Conta +1.
#   3. Se o contador chegou em k, achamos a resposta.
#   4. Senão, repete o processo a partir da subárvore direita desse nó.
#
# Tempo: O(h + k) — desce até o menor nó (altura h) e visita k nós.
# Espaço: O(h) — a pilha guarda no máximo um caminho da raiz até uma folha.
# ---------------------------------------------------------------------------
def k_esimo_menor_elemento(raiz, k):
    pilha = []
    no_atual = raiz
    quantidade_visitada = 0
 
    while pilha or no_atual is not None:
        while no_atual is not None:
            pilha.append(no_atual)
            no_atual = no_atual.esquerda
 
        no_atual = pilha.pop()
        quantidade_visitada += 1
 
        if quantidade_visitada == k:
            return no_atual.valor
 
        no_atual = no_atual.direita
 
    return None