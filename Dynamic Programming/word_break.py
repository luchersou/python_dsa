# ---------------------------------------------------------------------------
# 139. Word Break
# pode_quebrar[i] = True se o prefixo s[:i] pode ser dividido em palavras
# do dicionário. Para cada fim, procuramos um corte onde s[:corte] já é
# válido e s[corte:fim] é uma palavra.
# Tempo: O(n³)   (n² cortes, cada fatia/hash custa O(n))
# Espaço: O(n + tamanho do dicionário)
# ---------------------------------------------------------------------------
class Solucao:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dicionario = set(wordDict)
        pode_quebrar = [True] + [False] * len(s)  # prefixo vazio é sempre válido

        for fim in range(1, len(s) + 1):
            for corte in range(fim):
                if pode_quebrar[corte] and s[corte:fim] in dicionario:
                    pode_quebrar[fim] = True
                    break

        return pode_quebrar[len(s)]
