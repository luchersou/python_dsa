class Solucao:
    def jump(self, nums: list[int]) -> int:
        quantidade_saltos = 0
        fim_alcance_atual = 0
        alcance_maximo = 0

        # Não precisa avaliar o último índice, pois ali já é a chegada
        for posicao in range(len(nums) - 1):
            alcance_maximo = max(alcance_maximo, posicao + nums[posicao])

            # Quando chego no limite do alcance atual, sou obrigado
            # a dar mais um salto para poder ir além
            if posicao == fim_alcance_atual:
                quantidade_saltos += 1
                fim_alcance_atual = alcance_maximo

        return quantidade_saltos