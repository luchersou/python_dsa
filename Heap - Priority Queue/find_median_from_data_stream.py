import heapq


# ---------------------------------------------------------------------------
# 295. Find Median from Data Stream
# Dividimos os números em duas metades:
# - metade_menor: max-heap (guardamos valores negativos, pois o heapq é min-heap)
# - metade_maior: min-heap
# Mantemos metade_menor com o mesmo tamanho ou um elemento a mais.
# A mediana fica sempre no topo dos heaps.
# Tempo: O(log n) para adicionar, O(1) para a mediana
# Espaço: O(n)
# ---------------------------------------------------------------------------
class MedianFinder:
    def __init__(self):
        self.metade_menor = []
        self.metade_maior = []

    def adicionar_numero(self, numero: int) -> None:
        # Passa pela metade menor para garantir que o maior dela vá para a maior
        heapq.heappush(self.metade_menor, -numero)
        maior_da_metade_menor = -heapq.heappop(self.metade_menor)
        heapq.heappush(self.metade_maior, maior_da_metade_menor)

        # Rebalanceia: a metade menor nunca pode ficar menor que a maior
        if len(self.metade_maior) > len(self.metade_menor):
            menor_da_metade_maior = heapq.heappop(self.metade_maior)
            heapq.heappush(self.metade_menor, -menor_da_metade_maior)

    def encontrar_mediana(self) -> float:
        if len(self.metade_menor) > len(self.metade_maior):
            return float(-self.metade_menor[0])

        return (-self.metade_menor[0] + self.metade_maior[0]) / 2
