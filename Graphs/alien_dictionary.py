from collections import deque


class Solucao:
    def alienOrder(self, words: list[str]) -> str:
        # Cada letra aponta para as letras que vêm DEPOIS dela
        letras_seguintes = {letra: set() for palavra in words for letra in palavra}
        anteriores_pendentes = {letra: 0 for letra in letras_seguintes}

        # Compara palavras vizinhas para descobrir a ordem entre letras
        for palavra_a, palavra_b in zip(words, words[1:]):
            tamanho_minimo = min(len(palavra_a), len(palavra_b))

            # Caso inválido: "abc" aparece antes de "ab" (prefixo maior vem primeiro)
            if len(palavra_a) > len(palavra_b) and palavra_a[:tamanho_minimo] == palavra_b:
                return ""

            for posicao in range(tamanho_minimo):
                letra_a = palavra_a[posicao]
                letra_b = palavra_b[posicao]

                if letra_a != letra_b:
                    # Primeira diferença: letra_a vem antes de letra_b
                    if letra_b not in letras_seguintes[letra_a]:
                        letras_seguintes[letra_a].add(letra_b)
                        anteriores_pendentes[letra_b] += 1
                    break

        # Ordenação topológica: começa pelas letras sem nenhuma anterior pendente
        fila_de_disponiveis = deque(
            letra for letra in anteriores_pendentes
            if anteriores_pendentes[letra] == 0
        )

        ordem_das_letras = []

        while fila_de_disponiveis:
            letra = fila_de_disponiveis.popleft()
            ordem_das_letras.append(letra)

            for letra_seguinte in letras_seguintes[letra]:
                anteriores_pendentes[letra_seguinte] -= 1

                if anteriores_pendentes[letra_seguinte] == 0:
                    fila_de_disponiveis.append(letra_seguinte)

        # Se alguma letra ficou de fora, há um ciclo e a ordem é impossível
        if len(ordem_das_letras) < len(letras_seguintes):
            return ""

        return "".join(ordem_das_letras)