class Solucao:
    def numIslands(self, grid: list[list[str]]) -> int:
        linhas = len(grid)
        colunas = len(grid[0])
        visitados = set()
        quantidade_ilhas = 0

        def explorar_ilha(linha, coluna):
            posicoes_a_visitar = [(linha, coluna)]

            while posicoes_a_visitar:
                linha_atual, coluna_atual = posicoes_a_visitar.pop()

                fora_do_grid = (
                    linha_atual < 0 or linha_atual >= linhas or
                    coluna_atual < 0 or coluna_atual >= colunas
                )
                if fora_do_grid:
                    continue

                posicao = (linha_atual, coluna_atual)
                eh_agua = grid[linha_atual][coluna_atual] == "0"

                if posicao in visitados or eh_agua:
                    continue

                visitados.add(posicao)

                # Adiciona os quatro vizinhos (cima, baixo, esquerda, direita)
                posicoes_a_visitar.append((linha_atual + 1, coluna_atual))
                posicoes_a_visitar.append((linha_atual - 1, coluna_atual))
                posicoes_a_visitar.append((linha_atual, coluna_atual + 1))
                posicoes_a_visitar.append((linha_atual, coluna_atual - 1))

        for linha in range(linhas):
            for coluna in range(colunas):
                eh_terra_nao_visitada = grid[linha][coluna] == "1" and (linha, coluna) not in visitados

                if eh_terra_nao_visitada:
                    quantidade_ilhas += 1
                    explorar_ilha(linha, coluna)

        return quantidade_ilhas