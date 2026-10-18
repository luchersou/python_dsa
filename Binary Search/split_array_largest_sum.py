# ---------------------------------------------------------------------------
# 410. Split Array Largest Sum
# Em vez de procurar a divisão, buscamos a RESPOSTA: qual é a menor soma
# máxima permitida que ainda deixa dividir o array em no máximo k partes?
# - Limite inferior: o maior elemento (nenhuma parte pode ser menor que ele).
# - Limite superior: a soma de tudo (uma parte só).
# Para cada candidato, contamos de forma gulosa quantas partes precisamos.
# Tempo: O(n * log(soma total))
# Espaço: O(1)
# ---------------------------------------------------------------------------
def split_array(nums: list[int], k: int) -> int:
    def partes_necessarias(soma_maxima: int) -> int:
        # Vai enchendo a parte atual até estourar o limite, aí abre outra
        partes = 1
        soma_parte_atual = 0

        for numero in nums:
            if soma_parte_atual + numero > soma_maxima:
                partes += 1
                soma_parte_atual = 0
            soma_parte_atual += numero

        return partes

    esquerda, direita = max(nums), sum(nums)

    while esquerda < direita:
        meio = (esquerda + direita) // 2

        if partes_necessarias(meio) <= k:
            # Esse limite funciona; tenta um limite menor
            direita = meio
        else:
            # Limite pequeno demais, precisaria de mais de k partes
            esquerda = meio + 1

    return esquerda
