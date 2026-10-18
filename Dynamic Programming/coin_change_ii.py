# ---------------------------------------------------------------------------
# 518. Coin Change II
# formas[valor] = quantas combinações de moedas formam "valor".
# O laço de FORA é sobre as moedas: assim cada combinação é contada uma
# vez só, sem considerar a ordem (1+2 e 2+1 viram a mesma combinação).
# Se invertêssemos os laços, contaríamos permutações.
# Tempo: O(valor_alvo * m)   (m = quantidade de moedas)
# Espaço: O(valor_alvo)
# ---------------------------------------------------------------------------
class Solucao:
    def change(self, amount: int, coins: list[int]) -> int:
        formas = [1] + [0] * amount  # uma forma de formar 0: não usar moeda nenhuma

        for moeda in coins:
            for valor in range(moeda, amount + 1):
                formas[valor] += formas[valor - moeda]

        return formas[amount]
