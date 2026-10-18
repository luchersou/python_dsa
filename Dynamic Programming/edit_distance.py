# ---------------------------------------------------------------------------
# 72. Edit Distance
# tabela[i][j] = menor número de operações para transformar word1[:i]
# em word2[:j].
# - Caracteres iguais: não custa nada, tabela[i-1][j-1].
# - Diferentes: 1 + o menor entre
#     inserir   -> tabela[i][j-1]
#     remover   -> tabela[i-1][j]
#     substituir -> tabela[i-1][j-1]
# Caso base: transformar algo em string vazia custa o tamanho dela.
# Tempo: O(m * n)
# Espaço: O(m * n)
# ---------------------------------------------------------------------------
class Solucao:
    def minDistance(self, word1: str, word2: str) -> int:
        linhas, colunas = len(word1), len(word2)
        tabela = [[0] * (colunas + 1) for _ in range(linhas + 1)]

        for i in range(linhas + 1):
            tabela[i][0] = i  # remover todos os i caracteres
        for j in range(colunas + 1):
            tabela[0][j] = j  # inserir todos os j caracteres

        for i in range(1, linhas + 1):
            for j in range(1, colunas + 1):
                if word1[i - 1] == word2[j - 1]:
                    tabela[i][j] = tabela[i - 1][j - 1]
                else:
                    tabela[i][j] = 1 + min(
                        tabela[i][j - 1],      # inserir
                        tabela[i - 1][j],      # remover
                        tabela[i - 1][j - 1],  # substituir
                    )

        return tabela[linhas][colunas]
