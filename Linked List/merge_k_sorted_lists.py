import heapq


class No:
    def __init__(self, valor=0, proximo=None):
        self.valor = valor
        self.proximo = proximo


# ---------------------------------------------------------------------------
# 23. Merge k Sorted Lists
# Colocamos a cabeça de cada lista num min-heap. Sempre tiramos o menor,
# penduramos no resultado e colocamos no heap o próximo nó daquela lista.
# O índice da lista entra na tupla como desempate, porque nós não podem
# ser comparados entre si.
# Tempo: O(N log k)   (N = total de nós, k = quantidade de listas)
# Espaço: O(k)
# ---------------------------------------------------------------------------
def mesclar_k_listas(listas: list[No]) -> No:
    heap_minimo = []

    for indice_lista, cabeca in enumerate(listas):
        if cabeca is not None:
            heapq.heappush(heap_minimo, (cabeca.valor, indice_lista, cabeca))

    no_ficticio = No()
    atual = no_ficticio

    while heap_minimo:
        _, indice_lista, menor_no = heapq.heappop(heap_minimo)
        atual.proximo = menor_no
        atual = atual.proximo

        if menor_no.proximo is not None:
            heapq.heappush(heap_minimo, (menor_no.proximo.valor, indice_lista, menor_no.proximo))

    return no_ficticio.proximo
