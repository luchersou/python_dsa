def replace_elements(arr):
    resultado = [0] * len(arr)
    maior_ate_agora = -1
    
    # Percorre de trás pra frente
    for i in range(len(arr) - 1, -1, -1):
        resultado[i] = maior_ate_agora
        maior_ate_agora = max(maior_ate_agora, arr[i])
    
    return resultado