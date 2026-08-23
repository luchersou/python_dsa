from collections import defaultdict

def group_anagrams(strs):
    grupos = defaultdict(list)
    
    for palavra in strs:
        # Anagramas têm as mesmas letras, então a versão ordenada é igual
        chave = ''.join(sorted(palavra))
        grupos[chave].append(palavra)
    
    return list(grupos.values())