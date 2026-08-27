class Solucao:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        materias_dependentes = {materia: [] for materia in range(numCourses)}
        for materia, pre_requisito in prerequisites:
            materias_dependentes[pre_requisito].append(materia)

        # 0 = não visitada | 1 = sendo visitada agora (no caminho atual) | 2 = já concluída
        estado_da_materia = [0] * numCourses

        def existe_ciclo(materia):
            if estado_da_materia[materia] == 1:
                # Encontrou a mesma matéria no caminho atual: ciclo!
                return True

            if estado_da_materia[materia] == 2:
                # Já foi verificada antes e não gerou ciclo
                return False

            estado_da_materia[materia] = 1

            for proxima_materia in materias_dependentes[materia]:
                if existe_ciclo(proxima_materia):
                    return True

            estado_da_materia[materia] = 2
            return False

        for materia in range(numCourses):
            if existe_ciclo(materia):
                return False

        return True