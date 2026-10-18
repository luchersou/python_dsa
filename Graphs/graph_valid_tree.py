class Solucao:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # Uma árvore com n nós tem exatamente n - 1 arestas
        if len(edges) != n - 1:
            return False

        vizinhos = {no: [] for no in range(n)}
        for no_a, no_b in edges:
            vizinhos[no_a].append(no_b)
            vizinhos[no_b].append(no_a)

        visitados = set()
        nos_a_visitar = [0]

        while nos_a_visitar:
            no_atual = nos_a_visitar.pop()

            if no_atual in visitados:
                continue

            visitados.add(no_atual)
            nos_a_visitar.extend(vizinhos[no_atual])

        # Se todos os nós foram alcançados, o grafo é conexo
        return len(visitados) == n