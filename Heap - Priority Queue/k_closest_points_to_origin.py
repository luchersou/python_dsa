import heapq


class Solucao:
    def k_pontos_mais_proximos(self, pontos: list[list[int]], k: int) -> list[list[int]]:
        heap_maximo = []  # guarda tuplas (-distancia, ponto)

        for ponto in pontos:
            distancia = self._distancia_ao_quadrado(ponto)
            heapq.heappush(heap_maximo, (-distancia, ponto))

            if len(heap_maximo) > k:
                heapq.heappop(heap_maximo)

        return [ponto for _, ponto in heap_maximo]

    def _distancia_ao_quadrado(self, ponto: list[int]) -> int:
        x, y = ponto
        return x ** 2 + y ** 2