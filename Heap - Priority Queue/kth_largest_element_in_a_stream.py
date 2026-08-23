import heapq


class KthLargest:
    def __init__(self, k: int, numeros_iniciais: list[int]):
        self.k = k
        # mantemos um min-heap com no máximo k elementos:
        # o menor elemento desse heap é sempre o k-ésimo maior visto até agora
        self.heap_minimo = []

        for numero in numeros_iniciais:
            self.adicionar(numero)

    def adicionar(self, numero: int) -> int:
        heapq.heappush(self.heap_minimo, numero)

        if len(self.heap_minimo) > self.k:
            heapq.heappop(self.heap_minimo)

        return self.heap_minimo[0]