class No:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solucao:
    def cloneGraph(self, node: "No") -> "No":
        if node is None:
            return None

        nos_originais_para_clones = {}

        def clonar(no_original):
            if no_original in nos_originais_para_clones:
                return nos_originais_para_clones[no_original]

            no_clonado = No(no_original.val)
            nos_originais_para_clones[no_original] = no_clonado

            for vizinho in no_original.neighbors:
                no_clonado.neighbors.append(clonar(vizinho))

            return no_clonado

        return clonar(node)