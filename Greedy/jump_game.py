class Solucao:
    def canJump(self, nums: list[int]) -> bool:
        alcance_maximo = 0

        for posicao, salto in enumerate(nums):
            # Se a posição atual está além de onde eu conseguia alcançar,
            # é impossível ter chegado até aqui
            if posicao > alcance_maximo:
                return False

            alcance_maximo = max(alcance_maximo, posicao + salto)

        return True