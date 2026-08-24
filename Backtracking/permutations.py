def permutacoes(numeros: list[int]) -> list[list[int]]:
    """
    Gera todas as permutações possíveis de uma lista de números únicos.
    """
    resultado = []
    permutacao_atual = []
    numeros_usados = [False] * len(numeros)

    def backtrack():
        # Se a permutação atual já tem o tamanho da lista original, está completa
        if len(permutacao_atual) == len(numeros):
            resultado.append(permutacao_atual.copy())
            return

        for indice in range(len(numeros)):
            if numeros_usados[indice]:
                continue  # pula números já usados nessa permutação

            # Escolhe
            numeros_usados[indice] = True
            permutacao_atual.append(numeros[indice])

            # Explora
            backtrack()

            # Desfaz (backtrack)
            permutacao_atual.pop()
            numeros_usados[indice] = False

    backtrack()
    return resultado