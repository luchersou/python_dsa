def combinacoes_de_letras(digitos: str) -> list[str]:
    """
    Dado uma sequência de dígitos (2-9), retorna todas as combinações
    de letras que eles podem representar, como num teclado de telefone antigo.
    """
    if not digitos:
        return []

    mapa_digito_para_letras = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }

    resultado = []

    def backtrack(indice_digito: int, combinacao_atual: str):
        # Já formamos uma combinação do tamanho da entrada -> salva
        if indice_digito == len(digitos):
            resultado.append(combinacao_atual)
            return

        digito_atual = digitos[indice_digito]
        letras_possiveis = mapa_digito_para_letras[digito_atual]

        for letra in letras_possiveis:
            backtrack(indice_digito + 1, combinacao_atual + letra)

    backtrack(0, "")
    return resultado