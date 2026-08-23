from collections import defaultdict

def is_valid_sudoku(board):
    linhas = defaultdict(set)
    colunas = defaultdict(set)
    quadrantes = defaultdict(set)  # chave: (linha//3, coluna//3)
    
    for r in range(9):
        for c in range(9):
            valor = board[r][c]
            
            if valor == '.':
                continue
            
            quadrante_id = (r // 3, c // 3)
            
            # Se o valor já apareceu na linha, coluna ou quadrante, é inválido
            if (valor in linhas[r] or 
                valor in colunas[c] or 
                valor in quadrantes[quadrante_id]):
                return False
            
            linhas[r].add(valor)
            colunas[c].add(valor)
            quadrantes[quadrante_id].add(valor)
    
    return True