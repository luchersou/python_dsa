from collections import deque


class Solucao:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        palavras_disponiveis = set(wordList)

        if endWord not in palavras_disponiveis:
            return 0

        fila = deque([(beginWord, 1)])
        visitadas = {beginWord}
        letras = "abcdefghijklmnopqrstuvwxyz"

        while fila:
            palavra_atual, tamanho_do_caminho = fila.popleft()

            if palavra_atual == endWord:
                return tamanho_do_caminho

            for posicao in range(len(palavra_atual)):
                for letra in letras:
                    # Troca uma letra por vez, formando uma palavra vizinha
                    palavra_vizinha = (
                        palavra_atual[:posicao] + letra + palavra_atual[posicao + 1:]
                    )

                    if palavra_vizinha in palavras_disponiveis and palavra_vizinha not in visitadas:
                        visitadas.add(palavra_vizinha)
                        fila.append((palavra_vizinha, tamanho_do_caminho + 1))

        return 0