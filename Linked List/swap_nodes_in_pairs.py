def trocar_pares(cabeca: No) -> No:
    """
    Troca os nós em pares adjacentes.
    Ideia: usar um nó fictício antes da cabeça, e para cada par
    de nós, religar as três setas necessárias (fictício/anterior
    -> segundo, segundo -> primeiro, primeiro -> resto da lista).
    """
    no_fictício = No(valor=None, proximo=cabeca)
    no_anterior_ao_par = no_fictício

    while no_anterior_ao_par.proximo is not None and no_anterior_ao_par.proximo.proximo is not None:
        primeiro = no_anterior_ao_par.proximo
        segundo = primeiro.proximo

        # religa as setas para trocar a ordem do par
        primeiro.proximo = segundo.proximo
        segundo.proximo = primeiro
        no_anterior_ao_par.proximo = segundo

        # avança para o próximo par
        no_anterior_ao_par = primeiro

    return no_fictício.proximo