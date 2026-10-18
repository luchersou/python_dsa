# ---------------------------------------------------------------------------
# 57. Insert Interval
# Os intervalos já estão ordenados e não se sobrepõem. Percorremos em três
# fases:
# 1. Intervalos que terminam antes do novo começar: entram como estão.
# 2. Intervalos que se sobrepõem ao novo: mesclamos todos com ele.
# 3. Intervalos que começam depois do novo terminar: entram como estão.
# Tempo: O(n)
# Espaço: O(n) para o resultado
# ---------------------------------------------------------------------------
class Solucao:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        resultado = []
        novo_inicio, novo_fim = newInterval
        indice = 0

        while indice < len(intervals) and intervals[indice][1] < novo_inicio:
            resultado.append(intervals[indice])
            indice += 1

        while indice < len(intervals) and intervals[indice][0] <= novo_fim:
            novo_inicio = min(novo_inicio, intervals[indice][0])
            novo_fim = max(novo_fim, intervals[indice][1])
            indice += 1
        resultado.append([novo_inicio, novo_fim])

        resultado.extend(intervals[indice:])

        return resultado
