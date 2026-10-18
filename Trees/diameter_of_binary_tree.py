class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


def diametro_arvore(raiz):
    maior_diametro = 0
 
    def altura(no):
        nonlocal maior_diametro
 
        if no is None:
            return 0
 
        altura_esquerda = altura(no.esquerda)
        altura_direita = altura(no.direita)
 
        maior_diametro = max(maior_diametro, altura_esquerda + altura_direita)
 
        return 1 + max(altura_esquerda, altura_direita)
 
    altura(raiz)
    return maior_diametro