class Solucao:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        tanque_total = 0
        tanque_atual = 0
        posicao_de_partida = 0

        for posicao in range(len(gas)):
            saldo_do_posto = gas[posicao] - cost[posicao]
            tanque_total += saldo_do_posto
            tanque_atual += saldo_do_posto

            if tanque_atual < 0:
                # Não é possível chegar até aqui partindo do início atual,
                # então o próximo posto vira o novo candidato de partida
                posicao_de_partida = posicao + 1
                tanque_atual = 0

        # Se a soma total é negativa, não existe solução possível
        return posicao_de_partida if tanque_total >= 0 else -1