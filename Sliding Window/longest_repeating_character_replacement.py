from collections import Counter

def character_replacement(s, k):
    contagem = Counter()
    esquerda = 0
    maior_janela = 0

    for direita in range(len(s)):
        contagem[s[direita]] += 1

        tamanho_janela = direita - esquerda + 1
        caractere_mais_frequente = max(contagem.values())
        trocas_necessarias = tamanho_janela - caractere_mais_frequente

        # Se precisar de mais trocas do que k, encolhe a janela pela esquerda
        if trocas_necessarias > k:
            contagem[s[esquerda]] -= 1
            esquerda += 1

        tamanho_janela_atual = direita - esquerda + 1
        maior_janela = max(maior_janela, tamanho_janela_atual)

    return maior_janela