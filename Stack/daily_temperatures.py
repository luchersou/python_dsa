def daily_temperatures(temperatures):
    resultado = [0] * len(temperatures)
    pilha_indices = []  # guarda índices de dias esperando por um dia mais quente

    for dia_atual, temperatura_atual in enumerate(temperatures):
        # Enquanto o dia atual for mais quente que o topo da pilha, resolve o topo
        while pilha_indices and temperatura_atual > temperatures[pilha_indices[-1]]:
            dia_anterior = pilha_indices.pop()
            resultado[dia_anterior] = dia_atual - dia_anterior

        pilha_indices.append(dia_atual)

    return resultado