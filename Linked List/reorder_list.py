def reordenar_lista(cabeca: No) -> None:
    """
    Reordena a lista no padrão: primeiro, último, segundo,
    penúltimo, terceiro, antepenúltimo...

    Estratégia em 3 passos (cada um simples e testável sozinho):
    1. Achar o meio da lista (ponteiro lento/rápido)
    2. Inverter a segunda metade
    3. Intercalar as duas metades
    """
    if cabeca is None or cabeca.proximo is None:
        return

    # PASSO 1: achar o meio
    lento = cabeca
    rapido = cabeca
    while rapido.proximo is not None and rapido.proximo.proximo is not None:
        lento = lento.proximo
        rapido = rapido.proximo.proximo

    # separa a lista em duas: primeira_metade e segunda_metade
    segunda_metade = lento.proximo
    lento.proximo = None  # corta a ligação entre as duas metades
    primeira_metade = cabeca

    # PASSO 2: inverter a segunda metade (mesma lógica do exercício 52)
    anterior = None
    atual = segunda_metade
    while atual is not None:
        proximo_no = atual.proximo
        atual.proximo = anterior
        anterior = atual
        atual = proximo_no
    segunda_metade = anterior  # nova cabeça da segunda metade, agora invertida

    # PASSO 3: intercalar primeira_metade e segunda_metade
    while segunda_metade is not None:
        proximo_primeira = primeira_metade.proximo
        proximo_segunda = segunda_metade.proximo

        primeira_metade.proximo = segunda_metade
        segunda_metade.proximo = proximo_primeira

        primeira_metade = proximo_primeira
        segunda_metade = proximo_segunda