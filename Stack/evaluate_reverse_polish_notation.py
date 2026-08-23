def eval_rpn(tokens):
    pilha = []
    operadores = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operadores:
            # Retira os dois últimos números (a ordem importa para - e /)
            numero_2 = pilha.pop()
            numero_1 = pilha.pop()

            if token == '+':
                resultado = numero_1 + numero_2
            elif token == '-':
                resultado = numero_1 - numero_2
            elif token == '*':
                resultado = numero_1 * numero_2
            else:  # divisão
                # int() trunca em direção a zero, como pedido no problema
                resultado = int(numero_1 / numero_2)

            pilha.append(resultado)
        else:
            pilha.append(int(token))

    return pilha[0]