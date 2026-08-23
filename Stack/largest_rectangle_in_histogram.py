def largest_rectangle_area(heights):
    maior_area = 0
    pilha = []  # cada elemento é (indice_inicial, altura)

    for indice_atual, altura_atual in enumerate(heights):
        indice_inicial = indice_atual

        # Enquanto a barra atual for menor que o topo da pilha,
        # a barra do topo não consegue mais se expandir para a direita
        while pilha and pilha[-1][1] > altura_atual:
            indice_anterior, altura_anterior = pilha.pop()
            largura = indice_atual - indice_anterior
            maior_area = max(maior_area, altura_anterior * largura)
            indice_inicial = indice_anterior  # a barra atual "herda" esse início

        pilha.append((indice_inicial, altura_atual))

    # Esvazia o que sobrou na pilha: essas barras se estendem até o fim do histograma
    for indice_inicial, altura in pilha:
        largura = len(heights) - indice_inicial
        maior_area = max(maior_area, altura * largura)

    return maior_area