def subconjuntos_com_duplicatas(numeros: list[int]) -> list[list[int]]:
    """
    Gera todos os subconjuntos únicos de uma lista que pode conter números duplicados.
    Ex: [1,2,2] -> [[], [1], [1,2], [1,2,2], [2], [2,2]]
    """
    numeros_ordenados = sorted(numeros)  # ordenar ajuda a agrupar duplicatas
    resultado = []

    def backtrack(indice_inicial: int, subconjunto_atual: list[int]):
        resultado.append(subconjunto_atual.copy())

        for indice in range(indice_inicial, len(numeros_ordenados)):
            # Pula duplicatas no MESMO nível de recursão, exceto a primeira ocorrência
            eh_duplicata = indice > indice_inicial and numeros_ordenados[indice] == numeros_ordenados[indice - 1]
            if eh_duplicata:
                continue

            subconjunto_atual.append(numeros_ordenados[indice])
            backtrack(indice + 1, subconjunto_atual)
            subconjunto_atual.pop()

    backtrack(0, [])
    return resultado