def length_of_longest_substring(s):
    caracteres_na_janela = set()
    esquerda = 0
    maior_tamanho = 0

    for direita in range(len(s)):
        # Enquanto o caractere atual já estiver na janela, encolhe pela esquerda
        while s[direita] in caracteres_na_janela:
            caracteres_na_janela.remove(s[esquerda])
            esquerda += 1

        caracteres_na_janela.add(s[direita])
        tamanho_atual = direita - esquerda + 1
        maior_tamanho = max(maior_tamanho, tamanho_atual)

    return maior_tamanho