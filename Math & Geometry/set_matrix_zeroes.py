# ---------------------------------------------------------------------------
# 73. Set Matrix Zeroes
# Usamos a primeira linha e a primeira coluna da própria matriz como
# marcadores de "essa coluna/linha deve virar zero". Como a célula [0][0]
# seria compartilhada pelas duas, guardamos à parte se a primeira coluna
# precisa ser zerada.
# Tempo: O(m * n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        linhas, colunas = len(matrix), len(matrix[0])
        zerar_primeira_coluna = False

        # 1. Marca as linhas e colunas que têm zero
        for linha in range(linhas):
            if matrix[linha][0] == 0:
                zerar_primeira_coluna = True
            for coluna in range(1, colunas):
                if matrix[linha][coluna] == 0:
                    matrix[linha][0] = 0
                    matrix[0][coluna] = 0

        # 2. Zera de baixo para cima, para não apagar os marcadores da linha 0
        #    antes de usá-los
        for linha in range(linhas - 1, -1, -1):
            for coluna in range(colunas - 1, 0, -1):
                if matrix[linha][0] == 0 or matrix[0][coluna] == 0:
                    matrix[linha][coluna] = 0
            if zerar_primeira_coluna:
                matrix[linha][0] = 0
