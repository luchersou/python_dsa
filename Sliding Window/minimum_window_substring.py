from collections import Counter

def min_window(s, t):
    if not t or len(t) > len(s):
        return ""

    contagem_necessaria = Counter(t)
    contagem_janela = Counter()

    caracteres_distintos_necessarios = len(contagem_necessaria)
    caracteres_satisfeitos = 0  # quantos caracteres de t já têm a quantidade exigida na janela

    esquerda = 0
    menor_tamanho = float('inf')
    inicio_melhor_janela = 0

    for direita in range(len(s)):
        caractere_entrando = s[direita]
        contagem_janela[caractere_entrando] += 1

        # Se acabou de atingir a quantidade exigida, esse caractere ficou satisfeito
        if (caractere_entrando in contagem_necessaria
                and contagem_janela[caractere_entrando] == contagem_necessaria[caractere_entrando]):
            caracteres_satisfeitos += 1

        # Janela válida: tenta encolher pela esquerda para achar a menor possível
        while caracteres_satisfeitos == caracteres_distintos_necessarios:
            tamanho_atual = direita - esquerda + 1
            if tamanho_atual < menor_tamanho:
                menor_tamanho = tamanho_atual
                inicio_melhor_janela = esquerda

            caractere_saindo = s[esquerda]
            contagem_janela[caractere_saindo] -= 1

            # Se caiu abaixo do exigido, esse caractere deixou de estar satisfeito
            if (caractere_saindo in contagem_necessaria
                    and contagem_janela[caractere_saindo] < contagem_necessaria[caractere_saindo]):
                caracteres_satisfeitos -= 1

            esquerda += 1

    if menor_tamanho == float('inf'):
        return ""
    return s[inicio_melhor_janela : inicio_melhor_janela + menor_tamanho]