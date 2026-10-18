# ---------------------------------------------------------------------------
# 54. Spiral Matrix
# Mantemos quatro limites (topo, base, esquerda, direita) e percorremos a
# borda: direita, baixo, esquerda, cima. A cada volta, fechamos os limites.
# As checagens no meio evitam repetir elementos quando sobra só uma linha
# ou uma coluna.
# Tempo: O(m * n)
# Espaço: O(1) além do resultado
# ---------------------------------------------------------------------------
class Solucao:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        resultado = []
        topo, base = 0, len(matrix) - 1
        esquerda, direita = 0, len(matrix[0]) - 1

        while topo <= base and esquerda <= direita:
            for coluna in range(esquerda, direita + 1):
                resultado.append(matrix[topo][coluna])
            topo += 1

            for linha in range(topo, base + 1):
                resultado.append(matrix[linha][direita])
            direita -= 1

            if topo <= base:
                for coluna in range(direita, esquerda - 1, -1):
                    resultado.append(matrix[base][coluna])
                base -= 1

            if esquerda <= direita:
                for linha in range(base, topo - 1, -1):
                    resultado.append(matrix[linha][esquerda])
                esquerda += 1

        return resultado
