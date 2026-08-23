def encontrar_numero_duplicado(numeros: list[int]) -> int:
    """
    Encontra o número duplicado tratando o array como se fosse
    uma lista encadeada: o valor de cada posição aponta para
    o índice da próxima posição a visitar.

    Como existe um número repetido, dois índices diferentes
    vão apontar pro mesmo lugar em algum momento — isso cria
    um ciclo, igual no exercício 54 (Linked List Cycle).
    Usamos a mesma técnica: Tartaruga e Lebre (Floyd).
    """
    lento = numeros[0]
    rapido = numeros[0]

    # FASE 1: encontrar um ponto de encontro dentro do ciclo
    while True:
        lento = numeros[lento]
        rapido = numeros[numeros[rapido]]
        if lento == rapido:
            break

    # FASE 2: encontrar o INÍCIO do ciclo (que é o número duplicado)
    # propriedade do algoritmo de Floyd: andando um ponteiro do
    # início e outro do ponto de encontro, na mesma velocidade,
    # eles se encontram exatamente no início do ciclo
    lento = numeros[0]
    while lento != rapido:
        lento = numeros[lento]
        rapido = numeros[rapido]

    return lento



def encontrar_numero_duplicado_simples(numeros: list[int]) -> int:
    """Versão mais simples de entender, com espaço extra O(n)."""
    numeros_vistos = set()
    for numero in numeros:
        if numero in numeros_vistos:
            return numero
        numeros_vistos.add(numero)