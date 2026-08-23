def inverter_lista(cabeca: No) -> No:
    """
    Inverte a lista encadeada e retorna a nova cabeça.
    Ideia: caminhar pela lista trocando a direção das setas
    (proximo) uma a uma, guardando sempre o nó anterior.
    """
    anterior = None
    atual = cabeca

    while atual is not None:
        proximo_no = atual.proximo  # guarda o próximo antes de perder a referência
        atual.proximo = anterior    # inverte a seta
        anterior = atual            # avança o "anterior"
        atual = proximo_no          # avança o "atual"

    return anterior  # anterior é a nova cabeça