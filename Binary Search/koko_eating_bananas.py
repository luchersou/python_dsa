import math


def min_eating_speed(piles: list[int], h: int) -> int:
    def horas_necessarias(velocidade: int) -> int:
        # Quantas horas Koko leva pra comer todas as pilhas
        # nessa velocidade (arredondando pra cima em cada pilha)
        return sum(math.ceil(pilha / velocidade) for pilha in piles)

    esquerda, direita = 1, max(piles)

    while esquerda < direita:
        meio = (esquerda + direita) // 2

        if horas_necessarias(meio) <= h:
            # Essa velocidade dá conta a tempo;
            # tenta achar uma velocidade menor ainda
            direita = meio
        else:
            # Muito lenta, precisa de mais velocidade
            esquerda = meio + 1

    return esquerda