class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    # Nó fantasma facilita remover o próprio head, se for o caso
    dummy = ListNode(0, head)
    
    rapido = dummy
    lento = dummy
    
    # Avança o ponteiro rápido n passos à frente
    for _ in range(n):
        rapido = rapido.next
    
    # Move os dois juntos até rapido chegar no fim
    while rapido.next:
        rapido = rapido.next
        lento = lento.next
    
    # 'lento' está logo antes do nó a ser removido
    lento.next = lento.next.next
    
    return dummy.next