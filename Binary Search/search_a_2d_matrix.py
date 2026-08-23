def search_matrix(matrix: list[list[int]], target: int) -> bool:
    linhas, colunas = len(matrix), len(matrix[0])
    esquerda, direita = 0, (linhas * colunas) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        # Converte o índice "achatado" (meio) para linha/coluna reais
        linha = meio // colunas
        coluna = meio % colunas
        valor = matrix[linha][coluna]

        if valor == target:
            return True
        elif valor < target:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return False