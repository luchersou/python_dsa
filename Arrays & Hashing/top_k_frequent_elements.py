from collections import Counter

def top_k_frequent(nums, k):
    contagem = Counter(nums)
    # Pega os k elementos com maior frequência
    mais_comuns = contagem.most_common(k)
    return [numero for numero, freq in mais_comuns]