class Solucao:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervalos_ordenados = sorted(intervals, key=lambda intervalo: intervalo[0])
        intervalos_mesclados = [intervalos_ordenados[0]]

        for inicio, fim in intervalos_ordenados[1:]:
            ultimo_inicio, ultimo_fim = intervalos_mesclados[-1]

            if inicio <= ultimo_fim:
                # Há sobreposição: estende o fim do último intervalo se necessário
                intervalos_mesclados[-1][1] = max(ultimo_fim, fim)
            else:
                # Não há sobreposição: adiciona como um novo intervalo
                intervalos_mesclados.append([inicio, fim])

        return intervalos_mesclados