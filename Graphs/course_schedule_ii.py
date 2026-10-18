from collections import deque


class Solucao:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        materias_dependentes = {materia: [] for materia in range(numCourses)}
        pre_requisitos_pendentes = [0] * numCourses

        for materia, pre_requisito in prerequisites:
            materias_dependentes[pre_requisito].append(materia)
            pre_requisitos_pendentes[materia] += 1

        # Começa pelas matérias que não exigem nenhum pré-requisito
        fila_de_disponiveis = deque(
            materia for materia in range(numCourses)
            if pre_requisitos_pendentes[materia] == 0
        )

        ordem_dos_cursos = []

        while fila_de_disponiveis:
            materia = fila_de_disponiveis.popleft()
            ordem_dos_cursos.append(materia)

            for materia_dependente in materias_dependentes[materia]:
                pre_requisitos_pendentes[materia_dependente] -= 1

                # Todos os pré-requisitos dela foram cumpridos
                if pre_requisitos_pendentes[materia_dependente] == 0:
                    fila_de_disponiveis.append(materia_dependente)

        # Se alguma matéria ficou de fora, havia um ciclo
        if len(ordem_dos_cursos) < numCourses:
            return []

        return ordem_dos_cursos