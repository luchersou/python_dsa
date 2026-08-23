from collections import defaultdict
from bisect import bisect_right


class TimeMap:
    def __init__(self):
        # Para cada chave, guarda uma lista de (timestamp, valor)
        # em ordem crescente de timestamp
        self.armazenamento = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.armazenamento[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entradas = self.armazenamento[key]

        if not entradas:
            return ""

        # Queremos a última entrada cujo timestamp seja <= timestamp buscado.
        # bisect_right acha onde 'timestamp' entraria na lista de timestamps,
        # então tudo antes desse ponto tem timestamp <= o buscado.
        timestamps = [t for t, _ in entradas]
        indice = bisect_right(timestamps, timestamp)

        if indice == 0:
            return ""  # nenhuma entrada com timestamp <= o buscado

        return entradas[indice - 1][1]