class Solucao:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        linhas = len(heights)
        colunas = len(heights[0])

        alcanca_pacifico = set()
        alcanca_atlantico = set()

        def explorar(linha, coluna, celulas_alcancadas):
            celulas_alcancadas.add((linha, coluna))
            altura_atual = heights[linha][coluna]

            vizinhos = [
                (linha + 1, coluna),
                (linha - 1, coluna),
                (linha, coluna + 1),
                (linha, coluna - 1),
            ]

            for vizinho_linha, vizinho_coluna in vizinhos:
                dentro_do_grid = (
                    0 <= vizinho_linha < linhas and
                    0 <= vizinho_coluna < colunas
                )
                if not dentro_do_grid:
                    continue

                if (vizinho_linha, vizinho_coluna) in celulas_alcancadas:
                    continue

                # Andando "de trás para frente": só sobe ou mantém a altura
                altura_do_vizinho = heights[vizinho_linha][vizinho_coluna]
                if altura_do_vizinho >= altura_atual:
                    explorar(vizinho_linha, vizinho_coluna, celulas_alcancadas)

        # Bordas do Pacífico: linha de cima e coluna da esquerda
        for coluna in range(colunas):
            explorar(0, coluna, alcanca_pacifico)
        for linha in range(linhas):
            explorar(linha, 0, alcanca_pacifico)

        # Bordas do Atlântico: linha de baixo e coluna da direita
        for coluna in range(colunas):
            explorar(linhas - 1, coluna, alcanca_atlantico)
        for linha in range(linhas):
            explorar(linha, colunas - 1, alcanca_atlantico)

        # A resposta são as células que alcançam os dois oceanos
        celulas_nos_dois_oceanos = alcanca_pacifico & alcanca_atlantico
        return [list(celula) for celula in celulas_nos_dois_oceanos]