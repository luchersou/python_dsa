def max_profit(prices):
    menor_preco = prices[0]
    maior_lucro = 0

    for preco_atual in prices:
        if preco_atual < menor_preco:
            menor_preco = preco_atual
        else:
            lucro = preco_atual - menor_preco
            maior_lucro = max(maior_lucro, lucro)

    return maior_lucro