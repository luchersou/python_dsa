# ---------------------------------------------------------------------------
# 252. Meeting Rooms (Premium)
# Uma pessoa consegue ir a todas as reuniões se nenhuma se sobrepõe.
# Ordenando por início, basta checar se alguma reunião começa antes da
# anterior terminar.
# Tempo: O(n log n)
# Espaço: O(n) por causa da ordenação
# ---------------------------------------------------------------------------
class Solucao:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        reunioes_ordenadas = sorted(intervals, key=lambda reuniao: reuniao[0])

        for indice in range(1, len(reunioes_ordenadas)):
            inicio_atual = reunioes_ordenadas[indice][0]
            fim_anterior = reunioes_ordenadas[indice - 1][1]

            if inicio_atual < fim_anterior:
                return False

        return True
