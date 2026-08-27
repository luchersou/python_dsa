class Solucao:
    def maxSubArray(self, nums: list[int]) -> int:
        soma_atual = nums[0]
        maior_soma = nums[0]

        for numero in nums[1:]:
            # Decide: vale mais continuar a subsequência anterior
            # ou começar uma nova a partir do número atual?
            soma_atual = max(numero, soma_atual + numero)
            maior_soma = max(maior_soma, soma_atual)

        return maior_soma