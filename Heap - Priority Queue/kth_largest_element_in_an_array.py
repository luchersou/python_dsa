import heapq


class Solucao:
    def encontrar_kth_maior(self, numeros: list[int], k: int) -> int:
        heap_minimo = []

        for numero in numeros:
            heapq.heappush(heap_minimo, numero)

            if len(heap_minimo) > k:
                heapq.heappop(heap_minimo)

        return heap_minimo[0]