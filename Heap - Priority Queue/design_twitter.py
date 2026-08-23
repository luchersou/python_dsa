import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.contador_de_tempo = 0  # serve como "relógio": quanto maior, mais recente
        self.tweets_por_usuario = defaultdict(list)  # usuario -> lista de (tempo, id_do_tweet)
        self.seguidos_por_usuario = defaultdict(set)  # usuario -> conjunto de usuarios que ele segue

    def postar_tweet(self, id_usuario: int, id_tweet: int) -> None:
        self.tweets_por_usuario[id_usuario].append((self.contador_de_tempo, id_tweet))
        self.contador_de_tempo -= 1  # decrescente: valores menores = mais recentes, facilita o heap depois

    def obter_feed_de_noticias(self, id_usuario: int) -> list[int]:
        heap_candidatos = []

        usuarios_relevantes = self.seguidos_por_usuario[id_usuario] | {id_usuario}

        for usuario in usuarios_relevantes:
            tweets_do_usuario = self.tweets_por_usuario[usuario]
            if tweets_do_usuario:
                indice_do_ultimo_tweet = len(tweets_do_usuario) - 1
                tempo, id_tweet = tweets_do_usuario[indice_do_ultimo_tweet]
                heapq.heappush(heap_candidatos, (tempo, id_tweet, usuario, indice_do_ultimo_tweet))

        os_dez_mais_recentes = []

        while heap_candidatos and len(os_dez_mais_recentes) < 10:
            tempo, id_tweet, usuario, indice_do_tweet = heapq.heappop(heap_candidatos)
            os_dez_mais_recentes.append(id_tweet)

            proximo_indice = indice_do_tweet - 1
            if proximo_indice >= 0:
                tweets_do_usuario = self.tweets_por_usuario[usuario]
                proximo_tempo, proximo_id_tweet = tweets_do_usuario[proximo_indice]
                heapq.heappush(heap_candidatos, (proximo_tempo, proximo_id_tweet, usuario, proximo_indice))

        return os_dez_mais_recentes

    def seguir(self, id_seguidor: int, id_seguido: int) -> None:
        if id_seguidor != id_seguido:
            self.seguidos_por_usuario[id_seguidor].add(id_seguido)

    def deixar_de_seguir(self, id_seguidor: int, id_seguido: int) -> None:
        self.seguidos_por_usuario[id_seguidor].discard(id_seguido)