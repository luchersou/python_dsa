def is_palindrome(s: str) -> bool:
    # Mantém só letras e números, tudo em minúsculo
    limpo = [c.lower() for c in s if c.isalnum()]
    
    esquerda, direita = 0, len(limpo) - 1
    
    while esquerda < direita:
        if limpo[esquerda] != limpo[direita]:
            return False
        esquerda += 1
        direita -= 1
    
    return True