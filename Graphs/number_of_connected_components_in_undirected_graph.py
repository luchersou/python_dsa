class Solucao:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        vizinhos = {no: [] for no in range(n)}
        for no_a, no_b in edges:
            vizinhos[no_a].append(no_b)
            vizinhos[no_b].append(no_a)

        visitados = set()
        quantidade_componentes = 0

        def visitar_componente(no):
            nos_a_visitar = [no]

            while nos_a_visitar:
                no_atual = nos_a_visitar.pop()

                if no_atual in visitados:
                    continue

                visitados.add(no_atual)
                nos_a_visitar.extend(vizinhos[no_atual])

        for no in range(n):
            if no not in visitados:
                # Achou um nó fora de qualquer componente já contado
                quantidade_componentes += 1
                visitar_componente(no)

        return quantidade_componentes