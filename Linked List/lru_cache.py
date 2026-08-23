class NoDuplo:
    """Nó de uma lista duplamente encadeada: aponta pra frente e pra trás."""
    def __init__(self, chave=None, valor=None):
        self.chave = chave
        self.valor = valor
        self.anterior = None
        self.proximo = None


class LRUCache:
    """
    Cache com capacidade limitada. Quando lota, remove o item
    usado menos recentemente (Least Recently Used).

    Estratégia: combinar um dicionário (acesso O(1) por chave)
    com uma lista duplamente encadeada (pra saber a ordem de uso).

    - Nós mais recentes ficam perto da cabeça (direita)
    - Nós mais antigos ficam perto da cauda (esquerda)
    - Toda vez que um item é usado (get ou put), ele vai pra cabeça
    - Quando precisa remover, remove o que está na cauda
    """

    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.chave_para_no = {}  # dicionário: chave -> nó correspondente

        # nós fictícios (sentinelas) marcam início e fim da lista,
        # assim nunca precisamos tratar "lista vazia" como caso especial
        self.cabeca = NoDuplo()
        self.cauda = NoDuplo()
        self.cabeca.proximo = self.cauda
        self.cauda.anterior = self.cabeca

    def _remover_no(self, no: NoDuplo) -> None:
        """Remove um nó de onde ele estiver na lista."""
        no.anterior.proximo = no.proximo
        no.proximo.anterior = no.anterior

    def _inserir_no_inicio(self, no: NoDuplo) -> None:
        """Insere um nó logo depois da cabeça (posição de 'mais recente')."""
        no.proximo = self.cabeca.proximo
        no.anterior = self.cabeca
        self.cabeca.proximo.anterior = no
        self.cabeca.proximo = no

    def get(self, chave: int) -> int:
        if chave not in self.chave_para_no:
            return -1

        no = self.chave_para_no[chave]
        self._remover_no(no)
        self._inserir_no_inicio(no)  # marca como recém-usado
        return no.valor

    def put(self, chave: int, valor: int) -> None:
        if chave in self.chave_para_no:
            # chave já existe: atualiza o valor e marca como recém-usada
            no = self.chave_para_no[chave]
            no.valor = valor
            self._remover_no(no)
            self._inserir_no_inicio(no)
            return

        if len(self.chave_para_no) >= self.capacidade:
            # cache cheio: remove o nó menos recentemente usado (perto da cauda)
            no_menos_usado = self.cauda.anterior
            self._remover_no(no_menos_usado)
            del self.chave_para_no[no_menos_usado.chave]

        novo_no = NoDuplo(chave, valor)
        self.chave_para_no[chave] = novo_no
        self._inserir_no_inicio(novo_no)