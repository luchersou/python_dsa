class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
 
 
# ---------------------------------------------------------------------------
# 75. Binary Tree Maximum Path Sum
# Um caminho pode começar e terminar em qualquer nó, mas não pode "se
# bifurcar" duas vezes: ele sobe de um lado, passa por um nó "topo" e
# desce do outro.
#
# Para cada nó, calculamos duas coisas diferentes:
#   1. A melhor soma de um caminho que PASSA por este nó como topo
#      (usa os dois lados) -> serve para atualizar a resposta final.
#   2. O melhor "ganho" que este nó pode oferecer ao pai (só pode
#      continuar por UM lado, senão o caminho se bifurca) -> é o que
#      a função retorna.
#
# Se o ganho de um lado for negativo, ignoramos esse lado (usamos 0),
# porque é melhor não incluí-lo no caminho.
# Tempo: O(n)
# Espaço: O(h)
# ---------------------------------------------------------------------------
def soma_maxima_do_caminho(raiz):
    maior_soma = float("-inf")
 
    def ganho_maximo(no):
        nonlocal maior_soma
 
        if no is None:
            return 0
 
        ganho_esquerda = max(0, ganho_maximo(no.esquerda))
        ganho_direita = max(0, ganho_maximo(no.direita))
 
        soma_passando_pelo_no = no.valor + ganho_esquerda + ganho_direita
        maior_soma = max(maior_soma, soma_passando_pelo_no)
 
        return no.valor + max(ganho_esquerda, ganho_direita)
 
    ganho_maximo(raiz)
    return maior_soma