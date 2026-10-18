class Solucao:
    def solve(self, board: list[list[str]]) -> None:
        linhas = len(board)
        colunas = len(board[0])

        def marcar_como_segura(linha, coluna):
            fora_do_grid = (
                linha < 0 or linha >= linhas or
                coluna < 0 or coluna >= colunas
            )
            if fora_do_grid or board[linha][coluna] != "O":
                return

            # Marca temporariamente: esse "O" está ligado à borda
            board[linha][coluna] = "S"

            marcar_como_segura(linha + 1, coluna)
            marcar_como_segura(linha - 1, coluna)
            marcar_como_segura(linha, coluna + 1)
            marcar_como_segura(linha, coluna - 1)

        # 1) Marca todos os "O" conectados às bordas como seguros
        for linha in range(linhas):
            marcar_como_segura(linha, 0)
            marcar_como_segura(linha, colunas - 1)
        for coluna in range(colunas):
            marcar_como_segura(0, coluna)
            marcar_como_segura(linhas - 1, coluna)

        # 2) Converte o que sobrou e restaura os seguros
        for linha in range(linhas):
            for coluna in range(colunas):
                if board[linha][coluna] == "O":
                    # "O" que não toca a borda: está cercado
                    board[linha][coluna] = "X"
                elif board[linha][coluna] == "S":
                    # Era seguro: volta ao original
                    board[linha][coluna] = "O"