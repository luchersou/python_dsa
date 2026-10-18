# ---------------------------------------------------------------------------
# 309. Best Time to Buy and Sell Stock with Cooldown
# Máquina de estados: a cada dia estamos em um de três estados.
# - com_acao:   segurando uma ação (comprei hoje ou já tinha)
# - vendi_hoje: acabei de vender (amanhã é cooldown)
# - descansando: sem ação e livre para comprar
# Tempo: O(n)
# Espaço: O(1)
# ---------------------------------------------------------------------------
class Solucao:
    def maxProfit(self, prices: list[int]) -> int:
        com_acao = float("-inf")  # impossível ter ação antes do primeiro dia
        vendi_hoje = 0
        descansando = 0

        for preco in prices:
            com_acao_anterior = com_acao

            # Continuo segurando, ou compro hoje (só se estava descansando)
            com_acao = max(com_acao, descansando - preco)
            # Descanso vem de já estar descansando ou de sair do cooldown
            descansando = max(descansando, vendi_hoje)
            # Vendo a ação que eu tinha ontem
            vendi_hoje = com_acao_anterior + preco

        return max(vendi_hoje, descansando)
