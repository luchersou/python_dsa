class No:
    """Nó de uma árvore binária."""
 
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

# ---------------------------------------------------------------------------
# 76. Serialize and Deserialize Binary Tree
# Transformamos a árvore em uma string e depois reconstruímos a árvore a
# partir dela.
#
# Estratégia: percurso em pré-ordem (raiz, esquerda, direita), marcando
# os filhos vazios com "N". Esses marcadores são o que permite
# reconstruir a estrutura exata, sem ambiguidade.
#
# Exemplo:  árvore    1          ->  "1,2,N,N,3,4,N,N,5,N,N"
#                    / \
#                   2   3
#                      / \
#                     4   5
#
# Tempo: O(n) para serializar e para desserializar.
# Espaço: O(n)
# ---------------------------------------------------------------------------
class Codificador:
    def serializar(self, raiz):
        valores = []
 
        def percorrer(no):
            if no is None:
                valores.append("N")
                return
 
            valores.append(str(no.valor))
            percorrer(no.esquerda)
            percorrer(no.direita)
 
        percorrer(raiz)
        return ",".join(valores)
 
    def desserializar(self, dados):
        valores = iter(dados.split(","))
 
        def construir():
            valor = next(valores)
 
            if valor == "N":
                return None
 
            no = No(int(valor))
            no.esquerda = construir()
            no.direita = construir()
            return no
 
        return construir()