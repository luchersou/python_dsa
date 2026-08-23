def tem_ciclo(cabeca: No) -> bool:
    """
    Detecta se a lista encadeada tem um ciclo.
    Ideia (Tartaruga e Lebre / Floyd): dois ponteiros andando
    em velocidades diferentes. Se houver ciclo, o rápido
    eventualmente "dá a volta" e encontra o lento de novo.
    """
    lento = cabeca
    rapido = cabeca

    while rapido is not None and rapido.proximo is not None:
        lento = lento.proximo
        rapido = rapido.proximo.proximo

        if lento is rapido:
            return True

    return False