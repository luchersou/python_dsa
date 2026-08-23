def simplify_path(path):
    pilha = []
    partes = path.split('/')

    for parte in partes:
        if parte == '' or parte == '.':
            # Ignora: string vazia (de barras duplicadas) ou diretório atual
            continue
        elif parte == '..':
            # Sobe um nível, se houver algum diretório na pilha
            if pilha:
                pilha.pop()
        else:
            # Nome de diretório válido: entra na pilha
            pilha.append(parte)

    return '/' + '/'.join(pilha)