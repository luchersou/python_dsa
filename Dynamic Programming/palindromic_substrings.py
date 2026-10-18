# ---------------------------------------------------------------------------
# 647. Palindromic Substrings
# Mesma ideia de expandir a partir do centro: cada expansão bem-sucedida
# é um palíndromo novo, então apenas contamos.
# Tempo: O(n²)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def countSubstrings(self, s: str) -> int:
        total_palindromos = 0

        for centro in range(len(s)):
            for esquerda, direita in ((centro, centro), (centro, centro + 1)):
                while esquerda >= 0 and direita < len(s) and s[esquerda] == s[direita]:
                    total_palindromos += 1
                    esquerda -= 1
                    direita += 1

        return total_palindromos
