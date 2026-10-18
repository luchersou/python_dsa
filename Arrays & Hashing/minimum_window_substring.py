from collections import Counter


# ---------------------------------------------------------------------------
# 76. Minimum Window Substring
# Janela deslizante: expandimos a direita até a janela conter todos os
# caracteres de t (com as quantidades certas); depois encolhemos a esquerda
# enquanto ela continuar válida, registrando a menor janela encontrada.
# "faltando" conta quantos caracteres de t ainda não estão cobertos.
# Tempo: O(m + n)   (m = len(s), n = len(t))
# Espaço: O(tamanho do alfabeto)
# ---------------------------------------------------------------------------
def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    precisa = Counter(t)  # quanto ainda falta de cada caractere (pode ficar negativo)
    faltando = len(t)

    inicio_melhor = 0
    tamanho_melhor = float("inf")
    esquerda = 0

    for direita, caractere in enumerate(s):
        if precisa[caractere] > 0:
            faltando -= 1
        precisa[caractere] -= 1

        # Janela válida: tenta encolher pela esquerda
        while faltando == 0:
            tamanho_atual = direita - esquerda + 1
            if tamanho_atual < tamanho_melhor:
                tamanho_melhor = tamanho_atual
                inicio_melhor = esquerda

            caractere_saindo = s[esquerda]
            precisa[caractere_saindo] += 1
            if precisa[caractere_saindo] > 0:
                # Tiramos um caractere que era necessário
                faltando += 1
            esquerda += 1

    if tamanho_melhor == float("inf"):
        return ""

    return s[inicio_melhor:inicio_melhor + tamanho_melhor]
