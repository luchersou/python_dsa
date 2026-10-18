# ---------------------------------------------------------------------------
# 253. Meeting Rooms II (Premium)
# Separamos os inícios e os fins e ordenamos cada lista. Andamos pelos
# inícios: se alguma reunião já terminou até esse momento, reaproveitamos
# a sala dela; senão, precisamos de uma sala nova.
# Tempo: O(n log n)
# Espaço: O(n)
# ---------------------------------------------------------------------------
class Solucao:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        inicios = sorted(reuniao[0] for reuniao in intervals)
        fins = sorted(reuniao[1] for reuniao in intervals)

        salas_necessarias = 0
        indice_fim = 0

        for inicio in inicios:
            if inicio >= fins[indice_fim]:
                # Uma reunião terminou: a sala dela fica livre para esta
                indice_fim += 1
            else:
                salas_necessarias += 1

        return salas_necessarias
