class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
 
 
# ---------------------------------------------------------------------------
# Count Good Nodes in Binary Tree
# Um nó é "bom" se nenhum nó no caminho da raiz até ele tem valor maior
# que o dele. Ou seja: o valor dele é maior ou igual ao maior valor visto
# até ali.
#
# Ideia: descer pela árvore carregando o maior valor encontrado no caminho
# (maior_ate_aqui). Em cada nó:
#   1. Se o valor dele >= maior_ate_aqui, ele é bom (conta 1).
#   2. Atualiza o maior valor do caminho.
#   3. Soma os bons nós das subárvores esquerda e direita, passando o
#      maior valor atualizado para baixo.
#
# A raiz sempre é boa, pois não há ninguém acima dela.
# Tempo: O(n) — visita cada nó uma vez.
# Espaço: O(h) — pilha de recursão com a altura da árvore.
# ---------------------------------------------------------------------------
def contar_nos_bons(raiz):
    def contar(no, maior_ate_aqui):
        if no is None:
            return 0
 
        no_e_bom = 1 if no.valor >= maior_ate_aqui else 0
 
        novo_maior = max(maior_ate_aqui, no.valor)
 
        bons_na_esquerda = contar(no.esquerda, novo_maior)
        bons_na_direita = contar(no.direita, novo_maior)
 
        return no_e_bom + bons_na_esquerda + bons_na_direita
 
    return contar(raiz, float("-inf"))