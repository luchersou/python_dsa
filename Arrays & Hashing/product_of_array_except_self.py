def product_except_self(nums):
    n = len(nums)
    resultado = [1] * n
    
    # Passo 1: produto de tudo que vem ANTES do índice i
    produto_esquerda = 1
    for i in range(n):
        resultado[i] = produto_esquerda
        produto_esquerda *= nums[i]
    
    # Passo 2: multiplica pelo produto de tudo que vem DEPOIS do índice i
    produto_direita = 1
    for i in range(n - 1, -1, -1):
        resultado[i] *= produto_direita
        produto_direita *= nums[i]
    
    return resultado