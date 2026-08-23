class NoComPonteiroAleatorio:
    def __init__(self, valor, proximo=None, aleatorio=None):
        self.valor = valor
        self.proximo = proximo
        self.aleatorio = aleatorio


def copiar_lista_com_ponteiro_aleatorio(cabeca: NoComPonteiroAleatorio) -> NoComPonteiroAleatorio:
    """
    Copia a lista, incluindo os ponteiros 'aleatorio'.
    Ideia: usar um dicionário para mapear "nó original" -> "nó copiado".
    Assim, quando formos ligar os ponteiros (proximo e aleatorio),
    já sabemos pra qual cópia cada ponteiro original deve apontar.
    """
    if cabeca is None:
        return None

    original_para_copia = {}

    # PASSO 1: cria todos os nós copiados (só com o valor, sem ligações ainda)
    atual = cabeca
    while atual is not None:
        original_para_copia[atual] = NoComPonteiroAleatorio(valor=atual.valor)
        atual = atual.proximo

    # PASSO 2: agora liga proximo e aleatorio de cada cópia
    atual = cabeca
    while atual is not None:
        copia_atual = original_para_copia[atual]
        copia_atual.proximo = original_para_copia.get(atual.proximo)
        copia_atual.aleatorio = original_para_copia.get(atual.aleatorio)
        atual = atual.proximo

    return original_para_copia[cabeca]