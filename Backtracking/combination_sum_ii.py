def soma_combinacoes_com_duplicatas(candidatos: list[int], alvo: int) -> list[list[int]]:
    """
    Encontra todas as combinações únicas que somam 'alvo'.
    A lista pode ter números duplicados, mas cada posição só pode ser usada uma vez.
    """
    candidatos_ordenados = sorted(candidatos)
    resultado = []

    def backtrack(indice_inicial: int, combinacao_atual: list[int], soma_atual: int):
        if soma_atual == alvo:
            resultado.append(combinacao_atual.copy())
            return

        for indice in range(indice_inicial, len(candidatos_ordenados)):
            numero = candidatos_ordenados[indice]

            # Poda: se já passou do alvo, os próximos também vão passar (lista ordenada)
            if soma_atual + numero > alvo:
                break

            # Pula duplicatas no MESMO nível de recursão
            eh_duplicata = indice > indice_inicial and numero == candidatos_ordenados[indice - 1]
            if eh_duplicata:
                continue

            combinacao_atual.append(numero)
            # indice + 1 pois cada posição só pode ser usada uma vez
            backtrack(indice + 1, combinacao_atual, soma_atual + numero)
            combinacao_atual.pop()

    backtrack(0, [], 0)
    return resultado