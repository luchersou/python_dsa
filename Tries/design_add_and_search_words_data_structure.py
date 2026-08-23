class NoDaTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_de_palavra = False


class DicionarioDePalavras:
    def __init__(self):
        self.raiz = NoDaTrie()

    def adicionar_palavra(self, palavra: str) -> None:
        no_atual = self.raiz
        for caractere in palavra:
            if caractere not in no_atual.filhos:
                no_atual.filhos[caractere] = NoDaTrie()
            no_atual = no_atual.filhos[caractere]
        no_atual.fim_de_palavra = True

    def buscar(self, palavra: str) -> bool:
        return self._buscar_a_partir_de(palavra, self.raiz)

    def _buscar_a_partir_de(self, palavra: str, no_atual: NoDaTrie) -> bool:
        for indice, caractere in enumerate(palavra):
            if caractere == ".":
                # curinga: tenta todos os filhos possíveis nesse ponto
                resto_da_palavra = palavra[indice + 1:]
                for filho in no_atual.filhos.values():
                    if self._buscar_a_partir_de(resto_da_palavra, filho):
                        return True
                return False
            else:
                if caractere not in no_atual.filhos:
                    return False
                no_atual = no_atual.filhos[caractere]

        return no_atual.fim_de_palavra