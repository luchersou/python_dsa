from collections import Counter

def check_inclusion(s1, s2):
    tamanho_janela = len(s1)
    contagem_alvo = Counter(s1)

    if tamanho_janela > len(s2):
        return False

    contagem_janela = Counter(s2[:tamanho_janela])

    if contagem_janela == contagem_alvo:
        return True

    for i in range(tamanho_janela, len(s2)):
        caractere_entrando = s2[i]
        caractere_saindo = s2[i - tamanho_janela]

        contagem_janela[caractere_entrando] += 1
        contagem_janela[caractere_saindo] -= 1

        # Remove do dicionário para a comparação com contagem_alvo funcionar certo
        if contagem_janela[caractere_saindo] == 0:
            del contagem_janela[caractere_saindo]

        if contagem_janela == contagem_alvo:
            return True

    return False