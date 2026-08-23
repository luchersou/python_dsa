def generate_parenthesis(n):
    resultado = []

    def backtrack(combinacao_atual, quantidade_abertos, quantidade_fechados):
        # Caso base: usamos todos os parênteses disponíveis
        if len(combinacao_atual) == 2 * n:
            resultado.append(combinacao_atual)
            return

        # Só pode abrir se ainda não usamos todos os '(' disponíveis
        if quantidade_abertos < n:
            backtrack(combinacao_atual + '(', quantidade_abertos + 1, quantidade_fechados)

        # Só pode fechar se houver mais abertos do que fechados
        if quantidade_fechados < quantidade_abertos:
            backtrack(combinacao_atual + ')', quantidade_abertos, quantidade_fechados + 1)

    backtrack('', 0, 0)
    return resultado