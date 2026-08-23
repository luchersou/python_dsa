def is_valid(s):
    pilha = []
    pares_correspondentes = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for caractere in s:
        if caractere in pares_correspondentes:
            # É um fechamento: precisa corresponder ao topo da pilha
            if not pilha or pilha[-1] != pares_correspondentes[caractere]:
                return False
            pilha.pop()
        else:
            # É uma abertura: empilha
            pilha.append(caractere)

    # Válido só se todas as aberturas foram fechadas
    return len(pilha) == 0