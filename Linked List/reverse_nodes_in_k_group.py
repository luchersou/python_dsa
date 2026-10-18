class No:
    def __init__(self, valor=0, proximo=None):
        self.valor = valor
        self.proximo = proximo


# ---------------------------------------------------------------------------
# 25. Reverse Nodes in k-Group
# Andamos de grupo em grupo. Para cada grupo:
# 1. Verificamos se ainda existem k nós; se não, o resto fica como está.
# 2. Invertemos os k nós (igual ao Reverse Linked List).
# 3. Religamos o grupo invertido com o que vem antes e depois.
# Tempo: O(n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
def inverter_em_grupos(cabeca: No, k: int) -> No:
    no_ficticio = No(proximo=cabeca)
    antes_do_grupo = no_ficticio

    while True:
        # Encontra o k-ésimo nó do grupo atual
        fim_do_grupo = antes_do_grupo
        for _ in range(k):
            fim_do_grupo = fim_do_grupo.proximo
            if fim_do_grupo is None:
                return no_ficticio.proximo

        depois_do_grupo = fim_do_grupo.proximo

        # Inverte o grupo; o primeiro nó passa a apontar para depois_do_grupo
        anterior = depois_do_grupo
        atual = antes_do_grupo.proximo
        while atual is not depois_do_grupo:
            proximo_no = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo_no

        # O antigo primeiro do grupo agora é o último
        inicio_antigo = antes_do_grupo.proximo
        antes_do_grupo.proximo = fim_do_grupo
        antes_do_grupo = inicio_antigo
