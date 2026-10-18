# ---------------------------------------------------------------------------
# 91. Decode Ways
# formas(i) = número de formas de decodificar os i primeiros dígitos.
# - Se o dígito i sozinho é válido (1-9), soma formas(i-1).
# - Se os dígitos i-1 e i juntos formam 10-26, soma formas(i-2).
# Tempo: O(n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def numDecodings(self, s: str) -> int:
        formas_dois_atras = 1  # string vazia: uma forma (não decodificar nada)
        formas_um_atras = 1 if s[0] != "0" else 0

        for indice in range(1, len(s)):
            formas_atual = 0

            if s[indice] != "0":
                formas_atual += formas_um_atras

            dois_digitos = int(s[indice - 1:indice + 1])
            if 10 <= dois_digitos <= 26:
                formas_atual += formas_dois_atras

            formas_dois_atras = formas_um_atras
            formas_um_atras = formas_atual

        return formas_um_atras
