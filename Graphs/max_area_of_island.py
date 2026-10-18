class Solucao:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        linhas = len(grid)
        colunas = len(grid[0])
        visitados = set()
        maior_area = 0

        def calcular_area(linha, coluna):
            fora_do_grid = (
                linha < 0 or linha >= linhas or
                coluna < 0 or coluna >= colunas
            )
            if fora_do_grid:
                return 0

            eh_agua = grid[linha][coluna] == 0
            if eh_agua or (linha, coluna) in visitados:
                return 0

            visitados.add((linha, coluna))

            # Conta a célula atual (1) + a área dos quatro vizinhos
            return (
                1
                + calcular_area(linha + 1, coluna)
                + calcular_area(linha - 1, coluna)
                + calcular_area(linha, coluna + 1)
                + calcular_area(linha, coluna - 1)
            )

        for linha in range(linhas):
            for coluna in range(colunas):
                area_da_ilha = calcular_area(linha, coluna)
                maior_area = max(maior_area, area_da_ilha)

        return maior_area