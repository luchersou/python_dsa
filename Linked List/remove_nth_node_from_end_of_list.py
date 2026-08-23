def remover_enesimo_do_fim(cabeca: No, n: int) -> No:
    """
    Remove o n-ésimo nó contando do fim da lista.
    Ideia: dois ponteiros com uma distância de n nós entre eles.
    Quando o ponteiro da frente chega ao fim, o de trás está
    exatamente no nó anterior ao que precisa ser removido.
    """
    no_fictício = No(valor=None, proximo=cabeca)
    ponteiro_frente = no_fictício
    ponteiro_tras = no_fictício

    # avança o ponteiro da frente n posições
    for _ in range(n):
        ponteiro_frente = ponteiro_frente.proximo

    # move os dois juntos até o da frente chegar no último nó
    while ponteiro_frente.proximo is not None:
        ponteiro_frente = ponteiro_frente.proximo
        ponteiro_tras = ponteiro_tras.proximo

    # ponteiro_tras agora está logo antes do nó a ser removido
    ponteiro_tras.proximo = ponteiro_tras.proximo.proximo

    return no_fictício.proximo