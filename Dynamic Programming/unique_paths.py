# ---------------------------------------------------------------------------
# 62. Unique Paths
# Só podemos andar para a direita ou para baixo, então:
# caminhos(linha, coluna) = caminhos(linha-1, coluna) + caminhos(linha, coluna-1).
# Basta guardar uma linha da tabela: caminhos_da_linha[coluna] já tem o
# valor "de cima" e caminhos_da_linha[coluna-1] tem o valor "da esquerda".
# Tempo: O(m * n)
# Espaço: O(n)
# ---------------------------------------------------------------------------
class Solucao:
    def uniquePaths(self, m: int, n: int) -> int:
        caminhos_da_linha = [1] * n  # a primeira linha só tem um caminho por célula

        for _ in range(1, m):
            for coluna in range(1, n):
                caminhos_da_linha[coluna] += caminhos_da_linha[coluna - 1]

        return caminhos_da_linha[-1]
