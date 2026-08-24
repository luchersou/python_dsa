def particionar_em_palindromos(texto: str) -> list[list[str]]:
    """
    Divide 'texto' em todas as combinações possíveis de substrings
    onde cada substring é um palíndromo.
    Ex: "aab" -> [["a","a","b"], ["aa","b"]]
    """
    resultado = []

    def eh_palindromo(sub_texto: str) -> bool:
        return sub_texto == sub_texto[::-1]

    def backtrack(indice_inicial: int, particao_atual: list[str]):
        # Chegou ao fim do texto -> a partição atual é válida
        if indice_inicial == len(texto):
            resultado.append(particao_atual.copy())
            return

        for indice_final in range(indice_inicial, len(texto)):
            pedaco = texto[indice_inicial:indice_final + 1]

            if eh_palindromo(pedaco):
                particao_atual.append(pedaco)
                backtrack(indice_final + 1, particao_atual)
                particao_atual.pop()  # desfaz a escolha

    backtrack(0, [])
    return resultado