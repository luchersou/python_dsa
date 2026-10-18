# ---------------------------------------------------------------------------
# 1143. Longest Common Subsequence
# tabela[i][j] = tamanho da LCS entre text1[:i] e text2[:j].
# - Se text1[i-1] == text2[j-1], esse caractere entra: tabela[i-1][j-1] + 1.
# - Senão, descartamos um caractere de um dos textos:
#   max(tabela[i-1][j], tabela[i][j-1]).
# Tempo: O(m * n)
# Espaço: O(m * n)
# ---------------------------------------------------------------------------
class Solucao:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        linhas, colunas = len(text1), len(text2)
        tabela = [[0] * (colunas + 1) for _ in range(linhas + 1)]

        for i in range(1, linhas + 1):
            for j in range(1, colunas + 1):
                if text1[i - 1] == text2[j - 1]:
                    tabela[i][j] = tabela[i - 1][j - 1] + 1
                else:
                    tabela[i][j] = max(tabela[i - 1][j], tabela[i][j - 1])

        return tabela[linhas][colunas]
