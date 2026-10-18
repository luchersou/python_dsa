# ---------------------------------------------------------------------------
# 97. Interleaving String
# tabela[i][j] = True se s3[:i+j] pode ser formada intercalando s1[:i]
# e s2[:j]. O próximo caractere de s3 vem de s1 ou de s2:
# - de s1: tabela[i-1][j] e s1[i-1] == s3[i+j-1]
# - de s2: tabela[i][j-1] e s2[j-1] == s3[i+j-1]
# Tempo: O(m * n)
# Espaço: O(m * n)
# ---------------------------------------------------------------------------
class Solucao:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        tamanho1, tamanho2 = len(s1), len(s2)

        if tamanho1 + tamanho2 != len(s3):
            return False

        tabela = [[False] * (tamanho2 + 1) for _ in range(tamanho1 + 1)]
        tabela[0][0] = True  # strings vazias formam string vazia

        for i in range(tamanho1 + 1):
            for j in range(tamanho2 + 1):
                proximo_de_s3 = i + j - 1

                if i > 0 and tabela[i - 1][j] and s1[i - 1] == s3[proximo_de_s3]:
                    tabela[i][j] = True
                if j > 0 and tabela[i][j - 1] and s2[j - 1] == s3[proximo_de_s3]:
                    tabela[i][j] = True

        return tabela[tamanho1][tamanho2]
