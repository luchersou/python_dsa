# ---------------------------------------------------------------------------
# 72. Validate Binary Search Tree
# Não basta comparar cada nó só com os filhos diretos — um nó lá embaixo
# na subárvore direita, por exemplo, também precisa ser maior que TODOS os
# ancestrais à esquerda, não só o pai. Por isso vamos carregando um
# intervalo (limite_minimo, limite_maximo) válido para cada nó.
# Tempo: O(n)
# Espaço: O(h)
# ---------------------------------------------------------------------------
def e_arvore_busca_valida(raiz):
    def validar(no, limite_minimo, limite_maximo):
        if no is None:
            return True
 
        if not (limite_minimo < no.valor < limite_maximo):
            return False
 
        esquerda_valida = validar(no.esquerda, limite_minimo, no.valor)
        direita_valida = validar(no.direita, no.valor, limite_maximo)
 
        return esquerda_valida and direita_valida
 
    return validar(raiz, float("-inf"), float("inf"))