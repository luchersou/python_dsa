# ---------------------------------------------------------------------------
# 322. Coin Change
# menor_quantidade[valor] = menor número de moedas para formar "valor".
# Para cada valor, testamos usar cada moeda como a última:
# menor_quantidade[valor] = 1 + menor_quantidade[valor - moeda].
# Tempo: O(valor_alvo * m)   (m = quantidade de moedas)
# Espaço: O(valor_alvo)
# ---------------------------------------------------------------------------
class Solucao:
    def coinChange(self, coins: list[int], amount: int) -> int:
        impossivel = amount + 1  # mais moedas do que qualquer resposta real
        menor_quantidade = [0] + [impossivel] * amount

        for valor in range(1, amount + 1):
            for moeda in coins:
                if moeda <= valor:
                    menor_quantidade[valor] = min(
                        menor_quantidade[valor],
                        1 + menor_quantidade[valor - moeda],
                    )

        return menor_quantidade[amount] if menor_quantidade[amount] != impossivel else -1
