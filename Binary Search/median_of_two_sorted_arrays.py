# ---------------------------------------------------------------------------
# 4. Median of Two Sorted Arrays
# Fazemos busca binária no MENOR array para escolher quantos elementos dele
# ficam na metade esquerda. O resto da metade esquerda vem do outro array.
# A partição está correta quando todo elemento da esquerda é <= todo
# elemento da direita, ou seja:
#   maior_esquerda_a <= menor_direita_b  e  maior_esquerda_b <= menor_direita_a
# Tempo: O(log(min(m, n)))
# Espaço: O(1)
# ---------------------------------------------------------------------------
def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    menor, maior = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
    total = len(menor) + len(maior)
    tamanho_metade_esquerda = (total + 1) // 2

    esquerda, direita = 0, len(menor)

    while esquerda <= direita:
        # Quantos elementos de cada array vão para a metade esquerda
        corte_menor = (esquerda + direita) // 2
        corte_maior = tamanho_metade_esquerda - corte_menor

        # Infinito nas bordas para que a comparação sempre passe
        maior_esquerda_menor = menor[corte_menor - 1] if corte_menor > 0 else float("-inf")
        menor_direita_menor = menor[corte_menor] if corte_menor < len(menor) else float("inf")
        maior_esquerda_maior = maior[corte_maior - 1] if corte_maior > 0 else float("-inf")
        menor_direita_maior = maior[corte_maior] if corte_maior < len(maior) else float("inf")

        if maior_esquerda_menor <= menor_direita_maior and maior_esquerda_maior <= menor_direita_menor:
            # Partição correta
            maior_da_esquerda = max(maior_esquerda_menor, maior_esquerda_maior)

            if total % 2 == 1:
                return float(maior_da_esquerda)

            menor_da_direita = min(menor_direita_menor, menor_direita_maior)
            return (maior_da_esquerda + menor_da_direita) / 2
        elif maior_esquerda_menor > menor_direita_maior:
            # Pegamos elementos demais do array menor
            direita = corte_menor - 1
        else:
            # Pegamos elementos de menos do array menor
            esquerda = corte_menor + 1

    raise ValueError("Os arrays de entrada precisam estar ordenados")
