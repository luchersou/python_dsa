# ---------------------------------------------------------------------------
# 3. Longest Substring Without Repeating Characters
# Janela deslizante: guardamos a última posição em que vimos cada caractere.
# Se o caractere atual já apareceu DENTRO da janela, pulamos o início da
# janela para logo depois dessa ocorrência.
# Tempo: O(n)
# Espaço: O(min(n, tamanho do alfabeto))
# ---------------------------------------------------------------------------
def length_of_longest_substring(s: str) -> int:
    ultima_posicao = {}
    inicio_janela = 0
    maior_tamanho = 0

    for posicao, caractere in enumerate(s):
        if caractere in ultima_posicao and ultima_posicao[caractere] >= inicio_janela:
            inicio_janela = ultima_posicao[caractere] + 1

        ultima_posicao[caractere] = posicao
        maior_tamanho = max(maior_tamanho, posicao - inicio_janela + 1)

    return maior_tamanho
