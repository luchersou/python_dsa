class MinStack:
    def __init__(self):
        self.pilha_valores = []
        self.pilha_minimos = []

    def push(self, valor):
        self.pilha_valores.append(valor)

        # O topo da pilha de mínimos é sempre o menor valor "ativo" até agora
        if not self.pilha_minimos or valor <= self.pilha_minimos[-1]:
            self.pilha_minimos.append(valor)
        else:
            self.pilha_minimos.append(self.pilha_minimos[-1])

    def pop(self):
        self.pilha_valores.pop()
        self.pilha_minimos.pop()

    def top(self):
        return self.pilha_valores[-1]

    def get_min(self):
        return self.pilha_minimos[-1]