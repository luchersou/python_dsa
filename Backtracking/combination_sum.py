def soma_combinacoes(candidatos: list[int], alvo: int) -> list[list[int]]:
    """
    Encontra todas as combinações únicas de 'candidatos' que somam 'alvo'.
    Cada número pode ser usado quantas vezes forem necessárias.
    """
    resultado = []

    def backtrack(indice_inicial: int, combinacao_atual: list[int], soma_atual: int):
        if soma_atual == alvo:
            resultado.append(combinacao_atual.copy())
            return
        if soma_atual > alvo:
            return  # passou do alvo, esse caminho não serve

        for indice in range(indice_inicial, len(candidatos)):
            numero = candidatos[indice]
            combinacao_atual.append(numero)
            # Passa o MESMO índice (não indice + 1), pois pode reutilizar o número
            backtrack(indice, combinacao_atual, soma_atual + numero)
            combinacao_atual.pop()

    backtrack(0, [], 0)
    return resultado