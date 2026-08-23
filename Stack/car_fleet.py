def car_fleet(target, position, speed):
    carros = sorted(zip(position, speed), reverse=True)  # do mais próximo ao mais longe do alvo
    pilha_tempos = []  # tempo de chegada de cada pelotão já formado

    for posicao_atual, velocidade_atual in carros:
        tempo_para_chegar = (target - posicao_atual) / velocidade_atual

        # Se o carro atual é mais lento (leva mais tempo) que o pelotão da frente,
        # ele não alcança: forma um novo pelotão
        if not pilha_tempos or tempo_para_chegar > pilha_tempos[-1]:
            pilha_tempos.append(tempo_para_chegar)
        # Caso contrário, ele alcança o pelotão da frente e "gruda" nele
        # (não faz nada, pois já pertence ao pelotão cujo tempo está no topo)

    return len(pilha_tempos)