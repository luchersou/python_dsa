class Solucao:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervalos_ordenados = sorted(intervals, key=lambda intervalo: intervalo[1])
        quantidade_removidos = 0
        fim_do_ultimo_mantido = intervalos_ordenados[0][1]

        for inicio, fim in intervalos_ordenados[1:]:
            if inicio < fim_do_ultimo_mantido:
                # Sobrepõe o último intervalo mantido: remove o atual
                quantidade_removidos += 1
            else:
                # Não sobrepõe: mantém e atualiza a referência
                fim_do_ultimo_mantido = fim

        return quantidade_removidos