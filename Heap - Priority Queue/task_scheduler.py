import heapq
from collections import Counter, deque


class Solucao:
    def menor_tempo_total(self, tarefas: list[str], tempo_de_espera: int) -> int:
        contagem_por_tarefa = Counter(tarefas)

        # max-heap com as contagens (negativas, pelo truque de sempre)
        heap_maximo = [-contagem for contagem in contagem_por_tarefa.values()]
        heapq.heapify(heap_maximo)

        fila_de_espera = deque()  # guarda tuplas (contagem_restante, momento_em_que_pode_voltar_ao_heap)
        tempo_atual = 0

        while heap_maximo or fila_de_espera:
            tempo_atual += 1

            if heap_maximo:
                contagem_restante = -heapq.heappop(heap_maximo) - 1  # executa uma unidade dessa tarefa
                if contagem_restante > 0:
                    momento_de_retorno = tempo_atual + tempo_de_espera
                    fila_de_espera.append((contagem_restante, momento_de_retorno))

            # tarefas que já cumpriram o tempo de espera voltam para o heap
            if fila_de_espera and fila_de_espera[0][1] == tempo_atual:
                contagem_restante, _ = fila_de_espera.popleft()
                heapq.heappush(heap_maximo, -contagem_restante)

        return tempo_atual