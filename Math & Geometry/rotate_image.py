# ---------------------------------------------------------------------------
# 48. Rotate Image
# Girar 90° no sentido horário = transpor (trocar linha por coluna) e
# depois inverter cada linha. Tudo é feito na própria matriz.
# Tempo: O(n²)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def rotate(self, matrix: list[list[int]]) -> None:
        tamanho = len(matrix)

        # Transpõe: só a metade acima da diagonal, senão desfaz a troca
        for linha in range(tamanho):
            for coluna in range(linha + 1, tamanho):
                matrix[linha][coluna], matrix[coluna][linha] = matrix[coluna][linha], matrix[linha][coluna]

        for linha in matrix:
            linha.reverse()
