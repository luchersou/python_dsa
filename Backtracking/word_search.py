def existe_palavra(tabuleiro: list[list[str]], palavra: str) -> bool:
    """
    Verifica se 'palavra' pode ser formada percorrendo células adjacentes
    (cima, baixo, esquerda, direita) do tabuleiro, sem repetir uma célula.
    """
    total_linhas = len(tabuleiro)
    total_colunas = len(tabuleiro[0])

    def backtrack(linha: int, coluna: int, indice_letra: int) -> bool:
        # Encontrou todas as letras da palavra
        if indice_letra == len(palavra):
            return True

        # Fora do tabuleiro ou letra não bate
        fora_do_tabuleiro = linha < 0 or linha >= total_linhas or coluna < 0 or coluna >= total_colunas
        if fora_do_tabuleiro or tabuleiro[linha][coluna] != palavra[indice_letra]:
            return False

        # Marca a célula como visitada temporariamente
        letra_original = tabuleiro[linha][coluna]
        tabuleiro[linha][coluna] = "#"

        # Explora os 4 vizinhos
        encontrou = (
            backtrack(linha + 1, coluna, indice_letra + 1) or
            backtrack(linha - 1, coluna, indice_letra + 1) or
            backtrack(linha, coluna + 1, indice_letra + 1) or
            backtrack(linha, coluna - 1, indice_letra + 1)
        )

        # Desfaz a marcação (backtrack)
        tabuleiro[linha][coluna] = letra_original

        return encontrou

    for linha in range(total_linhas):
        for coluna in range(total_colunas):
            if backtrack(linha, coluna, 0):
                return True

    return False