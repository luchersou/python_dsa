class NoDaTrie:
    def __init__(self):
        self.filhos = {}  # dicionário: caractere -> NoDaTrie
        self.fim_de_palavra = False


class Trie:
    def __init__(self):
        self.raiz = NoDaTrie()

    def inserir(self, palavra: str) -> None:
        no_atual = self.raiz
        for caractere in palavra:
            if caractere not in no_atual.filhos:
                no_atual.filhos[caractere] = NoDaTrie()
            no_atual = no_atual.filhos[caractere]
        no_atual.fim_de_palavra = True

    def buscar(self, palavra: str) -> bool:
        no_final = self._percorrer_ate(palavra)
        return no_final is not None and no_final.fim_de_palavra

    def comeca_com(self, prefixo: str) -> bool:
        return self._percorrer_ate(prefixo) is not None

    def _percorrer_ate(self, texto: str) -> NoDaTrie | None:
        """Anda pela trie seguindo os caracteres de `texto`.
        Retorna o nó final, ou None se o caminho não existir."""
        no_atual = self.raiz
        for caractere in texto:
            if caractere not in no_atual.filhos:
                return None
            no_atual = no_atual.filhos[caractere]
        return no_atual