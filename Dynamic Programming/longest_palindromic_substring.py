# ---------------------------------------------------------------------------
# 5. Longest Palindromic Substring
# Todo palíndromo tem um centro: um caractere (tamanho ímpar) ou o espaço
# entre dois caracteres (tamanho par). Para cada centro, expandimos para
# os lados enquanto as pontas forem iguais.
# Tempo: O(n²)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def longestPalindrome(self, s: str) -> str:
        inicio_melhor = 0
        tamanho_melhor = 0

        for centro in range(len(s)):
            for esquerda, direita in ((centro, centro), (centro, centro + 1)):
                while esquerda >= 0 and direita < len(s) and s[esquerda] == s[direita]:
                    esquerda -= 1
                    direita += 1

                # Saímos do laço um passo além do palíndromo válido
                tamanho_atual = direita - esquerda - 1
                if tamanho_atual > tamanho_melhor:
                    tamanho_melhor = tamanho_atual
                    inicio_melhor = esquerda + 1

        return s[inicio_melhor:inicio_melhor + tamanho_melhor]
