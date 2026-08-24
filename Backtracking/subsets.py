def subconjuntos(numeros: list[int]) -> list[list[int]]:
    """
    Gera todos os subconjuntos possíveis de uma lista de números únicos.
    Ex: [1,2,3] -> [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
    """
    resultado = []

    def backtrack(indice_inicial: int, subconjunto_atual: list[int]):
        # Toda vez que entramos aqui, o subconjunto atual já é válido -> salva
        resultado.append(subconjunto_atual.copy())

        for indice in range(indice_inicial, len(numeros)):
            # Escolhe o número
            subconjunto_atual.append(numeros[indice])
            # Explora as próximas escolhas a partir do próximo índice
            backtrack(indice + 1, subconjunto_atual)
            # Desfaz a escolha (backtrack)
            subconjunto_atual.pop()

    backtrack(0, [])
    return resultado