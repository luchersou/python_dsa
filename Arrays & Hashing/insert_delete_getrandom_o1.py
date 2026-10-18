import random


# ---------------------------------------------------------------------------
# 380. Insert Delete GetRandom O(1)
# Uma lista permite sortear em O(1), e um dicionário valor -> índice permite
# achar o elemento em O(1). Para remover em O(1) sem deixar buraco na lista,
# trocamos o elemento com o último e fazemos pop().
# Tempo: O(1) em média para insert, remove e getRandom
# Espaço: O(n)
# ---------------------------------------------------------------------------
class RandomizedSet:
    def __init__(self):
        self.valores = []
        self.indice_do_valor = {}

    def insert(self, val: int) -> bool:
        if val in self.indice_do_valor:
            return False

        self.indice_do_valor[val] = len(self.valores)
        self.valores.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indice_do_valor:
            return False

        # Move o último elemento para a posição do que será removido
        indice_removido = self.indice_do_valor[val]
        ultimo_valor = self.valores[-1]

        self.valores[indice_removido] = ultimo_valor
        self.indice_do_valor[ultimo_valor] = indice_removido

        self.valores.pop()
        del self.indice_do_valor[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.valores)
