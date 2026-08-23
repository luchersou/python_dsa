import heapq


class Solucao:
    def peso_da_ultima_pedra(self, pesos: list[int]) -> int:
        # heapq é min-heap; para simular max-heap, guardamos os pesos negativos
        heap_maximo = [-peso for peso in pesos]
        heapq.heapify(heap_maximo)

        while len(heap_maximo) > 1:
            maior_peso = -heapq.heappop(heap_maximo)
            segundo_maior_peso = -heapq.heappop(heap_maximo)

            if maior_peso != segundo_maior_peso:
                peso_restante = maior_peso - segundo_maior_peso
                heapq.heappush(heap_maximo, -peso_restante)

        return -heap_maximo[0] if heap_maximo else 0