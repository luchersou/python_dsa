class NoDaTrie:
    def __init__(self):
        self.filhos = {}
        self.palavra_completa = None  # guarda a palavra em si quando termina aqui


class Solucao:
    def buscar_palavras(self, tabuleiro: list[list[str]], palavras: list[str]) -> list[str]:
        raiz = self._montar_trie(palavras)

        self.tabuleiro = tabuleiro
        self.linhas = len(tabuleiro)
        self.colunas = len(tabuleiro[0])
        self.palavras_encontradas = set()

        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                self._dfs(linha, coluna, raiz)

        return list(self.palavras_encontradas)

    def _montar_trie(self, palavras: list[str]) -> NoDaTrie:
        raiz = NoDaTrie()
        for palavra in palavras:
            no_atual = raiz
            for caractere in palavra:
                if caractere not in no_atual.filhos:
                    no_atual.filhos[caractere] = NoDaTrie()
                no_atual = no_atual.filhos[caractere]
            no_atual.palavra_completa = palavra
        return raiz

    def _dfs(self, linha: int, coluna: int, no_atual: NoDaTrie) -> None:
        letra = self.tabuleiro[linha][coluna]

        # célula já visitada nesse caminho, ou letra não continua nenhum prefixo válido
        if letra == "#" or letra not in no_atual.filhos:
            return

        proximo_no = no_atual.filhos[letra]

        if proximo_no.palavra_completa is not None:
            self.palavras_encontradas.add(proximo_no.palavra_completa)
            # não damos "return" aqui: pode existir uma palavra maior que continua no mesmo caminho

        self.tabuleiro[linha][coluna] = "#"  # marca célula como visitada

        for delta_linha, delta_coluna in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nova_linha, nova_coluna = linha + delta_linha, coluna + delta_coluna
            if 0 <= nova_linha < self.linhas and 0 <= nova_coluna < self.colunas:
                self._dfs(nova_linha, nova_coluna, proximo_no)

        self.tabuleiro[linha][coluna] = letra  # desfaz a marcação (backtracking)