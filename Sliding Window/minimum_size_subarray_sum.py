def min_sub_array_len(target, nums):
    esquerda = 0
    soma_atual = 0
    menor_tamanho = float('inf')

    for direita in range(len(nums)):
        soma_atual += nums[direita]

        # Enquanto a soma for suficiente, tenta encolher a janela pela esquerda
        while soma_atual >= target:
            tamanho_atual = direita - esquerda + 1
            menor_tamanho = min(menor_tamanho, tamanho_atual)

            soma_atual -= nums[esquerda]
            esquerda += 1

    return menor_tamanho if menor_tamanho != float('inf') else 0