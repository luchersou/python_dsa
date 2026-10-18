from collections import Counter

def find_substring(s, words):
    if not s or not words:
        return []

    tamanho_palavra = len(words[0])
    quantidade_palavras = len(words)
    contagem_alvo = Counter(words)
    resultado = []

    # Cada deslocamento alinha a janela em uma "grade" diferente de palavras
    for deslocamento in range(tamanho_palavra):
        esquerda = deslocamento
        contagem_janela = Counter()
        palavras_na_janela = 0

        for direita in range(deslocamento, len(s) - tamanho_palavra + 1, tamanho_palavra):
            palavra_entrando = s[direita : direita + tamanho_palavra]

            if palavra_entrando in contagem_alvo:
                contagem_janela[palavra_entrando] += 1
                palavras_na_janela += 1

                # Palavra apareceu demais: encolhe pela esquerda até voltar ao limite
                while contagem_janela[palavra_entrando] > contagem_alvo[palavra_entrando]:
                    palavra_saindo = s[esquerda : esquerda + tamanho_palavra]
                    contagem_janela[palavra_saindo] -= 1
                    palavras_na_janela -= 1
                    esquerda += tamanho_palavra

                # Janela com todas as palavras na quantidade certa
                if palavras_na_janela == quantidade_palavras:
                    resultado.append(esquerda)
            else:
                # Palavra inválida: nenhuma janela que a contenha serve, recomeça depois dela
                contagem_janela.clear()
                palavras_na_janela = 0
                esquerda = direita + tamanho_palavra

    return resultado