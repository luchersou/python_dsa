def mesclar_listas_ordenadas(lista1: No, lista2: No) -> No:
    """
    Mescla duas listas já ordenadas em uma única lista ordenada.
    Ideia: usar um nó "fictício" (dummy) para simplificar a
    montagem da lista de resultado, e ir comparando os valores
    das duas listas, sempre escolhendo o menor.
    """
    no_fictício = No(valor=None)  # nó auxiliar, não faz parte do resultado
    atual = no_fictício

    while lista1 is not None and lista2 is not None:
        if lista1.valor <= lista2.valor:
            atual.proximo = lista1
            lista1 = lista1.proximo
        else:
            atual.proximo = lista2
            lista2 = lista2.proximo
        atual = atual.proximo

    # quando uma lista acaba, só "pendura" o resto da outra
    atual.proximo = lista1 if lista1 is not None else lista2

    return no_fictício.proximo  # pula o nó fictício