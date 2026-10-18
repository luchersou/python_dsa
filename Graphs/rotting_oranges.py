from collections import deque


class Solucao:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        linhas = len(grid)
        colunas = len(grid[0])

        fila_de_podres = deque()
        laranjas_frescas = 0

        for linha in range(linhas):
            for coluna in range(colunas):
                if grid[linha][coluna] == 2:
                    fila_de_podres.append((linha, coluna))
                elif grid[linha][coluna] == 1:
                    laranjas_frescas += 1

        minutos = 0
        direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while fila_de_podres and laranjas_frescas > 0:
            # Processa todas as laranjas podres do minuto atual de uma vez
            for _ in range(len(fila_de_podres)):
                linha, coluna = fila_de_podres.popleft()

                for mudanca_linha, mudanca_coluna in direcoes:
                    vizinho_linha = linha + mudanca_linha
                    vizinho_coluna = coluna + mudanca_coluna

                    dentro_do_grid = (
                        0 <= vizinho_linha < linhas and
                        0 <= vizinho_coluna < colunas
                    )
                    if dentro_do_grid and grid[vizinho_linha][vizinho_coluna] == 1:
                        grid[vizinho_linha][vizinho_coluna] = 2
                        laranjas_frescas -= 1
                        fila_de_podres.append((vizinho_linha, vizinho_coluna))

            minutos += 1

        # Se sobrou laranja fresca, ela estava isolada e nunca apodrece
        return minutos if laranjas_frescas == 0 else -1