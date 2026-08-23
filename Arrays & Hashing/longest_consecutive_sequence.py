def longest_consecutive(nums):
    conjunto = set(nums)
    maior_sequencia = 0
    
    for num in conjunto:
        # Só começa a contar se for o INÍCIO de uma sequência
        # (ou seja, num - 1 não existe no conjunto)
        if num - 1 not in conjunto:
            tamanho_atual = 1
            while num + tamanho_atual in conjunto:
                tamanho_atual += 1
            maior_sequencia = max(maior_sequencia, tamanho_atual)
    
    return maior_sequencia